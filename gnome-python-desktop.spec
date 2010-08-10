%define buildgnomeprint 1
%define build_evince 1
%define build_nautilusburn 0
%define build_brasero 0
%if %mdvver <= 200900
%define build_nautilusburn 1
%else
%define build_brasero 1
%endif

%define pygtk 2.10.3
%define gnomepython 2.10.0
%define oname gnome-python

Summary: GNOME Desktop bindings for Python
Name: gnome-python-desktop
Version: 2.31.1
Release: %mkrel 1
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%name-%{version}.tar.bz2
Patch0: gnome-python-desktop-2.25.1-fix-linkage.patch
#gw link plparser wrapper with gtk until it was update for 2.29
Patch1: gnome-python-desktop-2.29.1-totem-plparser-add-gtk.patch
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/
License: LGPLv2+ and GPLv2+
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%name-root
BuildRequires: pygtk2.0-devel >= %pygtk
BuildRequires: gnome-python-devel >= %gnomepython
BuildRequires: gnome-python-gconf >= %gnomepython
BuildRequires: python-devel >= 2.2
BuildRequires: libgnomeui2-devel >= 2.0.0
BuildRequires: gtksourceview1-devel >= 1.1.90
BuildRequires: libpanel-applet-devel >= 2.13.4
BuildRequires: evolution-data-server-devel
BuildRequires: libwnck-devel >= 2.19.3
BuildRequires: librsvg-devel
BuildRequires: libgnome-keyring-devel >= 0.5.0
BuildRequires: gnome-desktop-devel
BuildRequires: libgcrypt-devel
BuildRequires: bug-buddy
BuildRequires: libcanberra-devel
BuildRequires: x11-server-xvfb
Requires: gnome-python >= %gnomepython
Conflicts: gnome-python-extras < 2.13.3


%description
The gnome-python-desktop package contains the Python bindings for the
GNOME Desktop modules.

%package -n %oname-applet
Version: %{version}
Summary: Python bindings for GNOME Panel applets
Group: Development/GNOME and GTK+
Requires: %name = %version

%description -n %oname-applet
This module contains a wrapper that allows GNOME Panel applets to be
written in Python.

%package -n %oname-evolution
Version: %{version}
Summary: Python bindings for Evolution
Group: Development/GNOME and GTK+
Requires: %name = %version

%description -n %oname-evolution
This module contains a wrapper that allows Evolution extensions to be
written in Python.


%package -n %oname-gtksourceview
Version: %{version}
Summary: Python bindings for Gtksourceview
Group: Development/GNOME and GTK+
Requires: %oname-gnomeprint = %version

%description -n %oname-gtksourceview
This module contains a wrapper that makes Gtksourceview available from Python.

%package -n %oname-gtop
Version: %{version}
Summary: Python bindings for Gtop
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libgtop2.0-devel >= 2.13

%description -n %oname-gtop
This module contains a wrapper that makes Gtop available from Python.

%if %build_nautilusburn
%package -n %oname-nautilus-burn
Version: %{version}
Summary: Python bindings for Nautilus-burn
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libnautilus-burn-devel >= 2.15.3

%description -n %oname-nautilus-burn
This module contains a wrapper that makes Nautilus-burn available from Python.
%endif

%if %build_brasero
%package -n %oname-brasero
Version: %{version}
Summary: Python bindings for Brasero
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: brasero-devel

%description -n %oname-brasero
This module contains a wrapper that makes Brasero available from Python.
%endif

%package -n %oname-totem
Version: %{version}
Summary: Python bindings for the Totem playlist parser
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libtotem-plparser-devel

%description -n %oname-totem
This module contains a wrapper that makes the Totem playlist parser
available from Python.

%package -n %oname-mediaprofiles
Version: %{version}
Summary: Python bindings for the GNOME media profiles
Group: Development/GNOME and GTK+
Requires: %name = %version
Requires: gnome-python-gconf >= %gnomepython
BuildRequires: libcddb-slave2-devel

%description -n %oname-mediaprofiles
This module contains a wrapper that makes the GNOME media profiles library
available from Python.

%package -n %oname-metacity
Version: %{version}
Summary: Python bindings for the Metacity window manager
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libmetacity-private-devel >= 2.17.8

%description -n %oname-metacity
This module contains a wrapper that makes the Metacity window manager library
available from Python.

%if %{buildgnomeprint}
%package -n %oname-gnomeprint
Summary: Python bindings for interacting with gnomeprint and gnomeprintui
Group: Development/GNOME and GTK+
BuildRequires: libgnomeprintui-devel >= 2.8.0

%description -n %oname-gnomeprint
This module contains a wrapper that allows the use of gnomeprint and
gnomeprintui via python.
%endif

%if %build_evince
%package -n %oname-evince
Version: %{version}
Summary: Python bindings for the Evince document viewer
Group: Development/GNOME and GTK+
Requires: %name = %version
Obsoletes: python-evince
BuildRequires: libevince-devel >= 2.30.0

%description -n %oname-evince
This module contains a wrapper that makes the Evince document viewer library
available from Python.
%endif

%prep
%setup -q
%patch1 -p1
autoreconf -fi

%build
%configure2_5x --enable-metacity
%make

%check
# Disabled due to http://bugzilla.gnome.org/show_bug.cgi?id=565593 :
# check fails against Python 2.6 due to Python issue #4244 - AdamW
# 2008/12
#xvfb-run make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%doc examples/rsvg examples/keyring* examples/wnck*
%defattr(755,root,root,755)
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%_libdir/pkgconfig/%name-2.0.pc
%py_platsitedir/gtk-2.0/wnck.so
%py_platsitedir/gtk-2.0/rsvg.so
%py_platsitedir/gtk-2.0/gnomekeyring.so
%py_platsitedir/gtk-2.0/bugbuddy* 

%files -n %oname-applet
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gnome/applet.py*
%py_platsitedir/gtk-2.0/gnomeapplet.so
%py_platsitedir/gtk-2.0/gnomedesktop/
%doc examples/applet/

%files -n %oname-evolution
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/evolution

%files -n %oname-gtksourceview
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gtksourceview.so
%doc examples/gtksourceview
%doc %_datadir/gtk-doc/html/pygtksourceview

%files -n %oname-gtop
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gtop.so

%if %build_nautilusburn
%files -n %oname-nautilus-burn
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/nautilusburn.so
%doc examples/nautilusburn
%endif

%if %build_brasero
%files -n %oname-brasero
%defattr(755,root,root,755)
%doc examples/brasero*
%py_platsitedir/gtk-2.0/braseroburn.so
%py_platsitedir/gtk-2.0/braseromedia.so
%doc examples/braseromedia
%endif

%files -n %oname-totem
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/totem/

%files -n %oname-mediaprofiles
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/mediaprofiles.so
%doc examples/mediaprofiles

%files -n %oname-metacity
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/metacity.so

%if %{buildgnomeprint}
%files -n %oname-gnomeprint
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gnomeprint/
%doc examples/gnomeprint/
%_datadir/gtk-doc/html/pygnomeprint*
%endif

%if %build_evince
%files -n %oname-evince
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/evince.so
%endif
