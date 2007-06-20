%define buildgnomeprint 1
%define pygtk 2.4.0
%define gnomepython 2.10.0
%define oname gnome-python

Summary: GNOME Desktop bindings for Python
Name: gnome-python-desktop
Version: 2.18.0
Release: %mkrel 2
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%name-%{version}.tar.bz2
# From FreeBSD ports: fixes build against metacity 2.19 - AdamW 2007/06
Patch0:	gnome-python-desktop-2.18.0-metacity.patch
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/
License: LGPL
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%name-root
BuildRequires: pygtk2.0-devel >= %pygtk
BuildRequires: gnome-python >= %gnomepython
BuildRequires: python-devel >= 2.2
BuildRequires: libgnomeui2-devel >= 2.0.0
BuildRequires: libgtksourceview-1.0-devel >= 1.1.0
BuildRequires: libpanel-applet-devel >= 2.13
BuildRequires: libwnck-devel >= 2.15.5
BuildRequires: librsvg-devel
BuildRequires: gnome-keyring-devel >= 0.5.0
BuildRequires: gnome-desktop-devel
BuildRequires: bug-buddy
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

%package -n %oname-nautilus-burn
Version: %{version}
Summary: Python bindings for Nautilus-burn
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libnautilus-burn-devel >= 2.15.3

%description -n %oname-nautilus-burn
This module contains a wrapper that makes Nautilus-burn available from Python.

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

%prep
%setup -q
%patch0 -p0 -b .metacity

%build
%configure2_5x --enable-metacity

%make

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%doc examples/rsvg examples/keyring*
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

%files -n %oname-gtksourceview
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gtksourceview.so
%doc examples/gtksourceview
%doc %_datadir/gtk-doc/html/pygtksourceview

%files -n %oname-gtop
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gtop.so

%files -n %oname-nautilus-burn
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/nautilusburn.so
%doc examples/nautilusburn

%files -n %oname-totem
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/totem/

%files -n %oname-mediaprofiles
%defattr(755,root,root,755)
%_libdir/python%pyver/site-packages/gtk-2.0/mediaprofiles.so
%doc examples/mediaprofiles

%files -n %oname-metacity
%defattr(755,root,root,755)
%_libdir/python%pyver/site-packages/gtk-2.0/metacity.so

%if %{buildgnomeprint}
%files -n %oname-gnomeprint
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gnomeprint/
%doc examples/gnomeprint/
%_datadir/gtk-doc/html/pygnomeprint*
%endif


