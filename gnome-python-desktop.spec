%define url_ver %(echo %{version}|cut -d. -f1,2)

# evince, brasero and mediaprofiles are disabled because these things have
# been ported to GTK+3. It's not practical to mix GTK+2 and GTK+3 bindings
# in gnome-python2-desktop, so for now we'll just have to disable the GTK+3
# stuff. - AdamW 2010/07
%define build_brasero 0
%define build_evince 0
%define build_gnomeprint 1
%define build_mediaprofiles 0

%define pygtk 2.10.3
%define gnomepython 2.10.0
%define oname gnome-python

Summary:	GNOME Desktop bindings for Python
Name:		gnome-python-desktop
Version:	2.32.0
Release:	10
License:	LGPLv2+ and GPLv2+
Group:		Development/GNOME and GTK+
Url:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/%{url_ver}/%{name}-%{version}.tar.bz2
#gw link plparser wrapper with gtk until it was update for 2.29
Patch1:		gnome-python-desktop-2.29.1-totem-plparser-add-gtk.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=672016
Patch2:		gnome-python-desktop-2.32.0-metacity-build.patch
Patch3:		gnome-python-desktop-2.32.0-automake-1.13.patch

BuildRequires:	gnome-python-gconf >= %{gnomepython}
BuildRequires:	x11-server-xvfb
BuildRequires:	pkgconfig(gnome-desktop-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1) >= 0.5.0
BuildRequires:	pkgconfig(gnome-python-2.0) >= %{gnomepython}
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)

%description
The gnome-python-desktop package contains the Python bindings for the
GNOME Desktop modules.

%package -n %{oname}-gnomekeyring
Summary:	Python bindings for Gnome-keyring
Group:		Development/GNOME and GTK+
Requires:	gnome-keyring
Conflicts:	gnome-python-desktop < 2.32.0-5

%description -n %{oname}-gnomekeyring
This module contains a wrapper that makes Gnome-keyring available from Python.

%package -n %{oname}-gtksourceview
Summary:	Python bindings for Gtksourceview
Group:		Development/GNOME and GTK+
Requires:	gtksourceview1
Requires:	%{oname}-gnomeprint = %{version}
Conflicts:	gnome-python-desktop < 2.32.0-5

%description -n %{oname}-gtksourceview
This module contains a wrapper that makes Gtksourceview available from Python.

%package -n %{oname}-gtop
Summary:	Python bindings for Gtop
Group:		Development/GNOME and GTK+
Requires:	libgtop2
BuildRequires:	pkgconfig(libgtop-2.0)

%description -n %{oname}-gtop
This module contains a wrapper that makes Gtop available from Python.

%if %{build_brasero}
%package -n %{oname}-brasero
Summary:	Python bindings for Brasero
Group:		Development/GNOME and GTK+
Requires:	brasero
BuildRequires:	brasero-devel

%description -n %{oname}-brasero
This module contains a wrapper that makes Brasero available from Python.
%endif

%package -n %{oname}-totem
Summary:	Python bindings for the Totem playlist parser
Group:		Development/GNOME and GTK+
BuildRequires:	pkgconfig(totem-plparser)

%description -n %{oname}-totem
This module contains a wrapper that makes the Totem playlist parser
available from Python.

%if %{build_mediaprofiles}
%package -n %{oname}-mediaprofiles
Summary:	Python bindings for the GNOME media profiles
Group:		Development/GNOME and GTK+
Requires:	gnome-media
Requires:	gnome-python-gconf >= %{gnomepython}
Conflicts:	gnome-python-desktop < 2.32.0-5
BuildRequires:	pkgconfig(gnome-media-profiles)

%description -n %{oname}-mediaprofiles
This module contains a wrapper that makes the GNOME media profiles library
available from Python.
%endif

%package -n %{oname}-metacity
Summary:	Python bindings for the Metacity window manager
Group:		Development/GNOME and GTK+
Requires:	metacity
Conflicts:	gnome-python-desktop < 2.32.0-5
BuildRequires:	pkgconfig(libmetacity-private)

%description -n %{oname}-metacity
This module contains a wrapper that makes the Metacity window manager library
available from Python.

%if %{build_gnomeprint}
%package -n %{oname}-gnomeprint
Summary:	Python bindings for interacting with gnomeprint and gnomeprintui
Group:		Development/GNOME and GTK+
Requires:	libgnomeprintui
Requires:	gnome-python-canvas
Conflicts:	gnome-python-desktop < 2.32.0-5
BuildRequires:	pkgconfig(libgnomeprintui-2.2)

%description -n %{oname}-gnomeprint
This module contains a wrapper that allows the use of gnomeprint and
gnomeprintui via python.
%endif

%if %{build_evince}
%package -n %{oname}-evince
Summary:	Python bindings for the Evince document viewer
Group:		Development/GNOME and GTK+
Requires:	evince
Conflicts:	gnome-python-desktop < 2.32.0-5
Obsoletes:	python-evince
BuildRequires:	evince-devel >= 2.31.90

%description -n %{oname}-evince
This module contains a wrapper that makes the Evince document viewer library
available from Python.
%endif

%package -n %{oname}-wnck
Summary:	Python-wnck bindings
Group:		Development/GNOME and GTK+
Requires:	libwnck
Conflicts:	gnome-python-desktop < 2.32.0-5

%description -n %{oname}-wnck
This package contains a module that allows communication with the Window
Manager using the EWMH specification from Python applications.

%package devel
Summary:	Pkgconfig file for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
Conflicts:	gnome-python-desktop < 2.32.0-5

%description devel
This package contains pkgconfig file for %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--enable-metacity \
	--disable-evince \
	--disable-braseromedia \
	--disable-braseroburn \
	--disable-mediaprofiles \
	--disable-gnomedesktop \
	--disable-applet

%make LIBS="`python-config --libs`"

%check
# Disabled due to http://bugzilla.gnome.org/show_bug.cgi?id=565593 :
# check fails against Python 2.6 due to Python issue #4244 - AdamW
# 2008/12
#xvfb-run make check

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%dir %{_datadir}/pygtk/2.0/defs
#%{py_platsitedir}/gtk-2.0/gnomedesktop/
%{py_platsitedir}/gtk-2.0/bugbuddy*
#%{_datadir}/pygtk/2.0/defs/_gnomedesktop.defs

%files -n %{oname}-gnomekeyring
%doc examples/keyring*
%{py_platsitedir}/gtk-2.0/gnomekeyring.so
%{_datadir}/pygtk/2.0/defs/gnomekeyring.defs

%files -n %{oname}-gtksourceview
%doc examples/gtksourceview
%{py_platsitedir}/gtk-2.0/gtksourceview.so
%{_datadir}/pygtk/2.0/defs/gtksourceview.defs
%doc %{_datadir}/gtk-doc/html/pygtksourceview

%files -n %{oname}-gtop
%{py_platsitedir}/gtk-2.0/gtop.so

%if %{build_brasero}
%files -n %{oname}-brasero
%doc examples/brasero*
%{py_platsitedir}/gtk-2.0/braseroburn.so
%{py_platsitedir}/gtk-2.0/braseromedia.so
%doc examples/braseromedia
%endif

%files -n %{oname}-totem
%{py_platsitedir}/gtk-2.0/totem/

%if %{build_mediaprofiles}
%files -n %{oname}-mediaprofiles
%doc examples/mediaprofiles
%{py_platsitedir}/gtk-2.0/mediaprofiles.so
%{_datadir}/pygtk/2.0/defs/mediaprofiles.defs
%endif

%files -n %{oname}-metacity
%{py_platsitedir}/gtk-2.0/metacity.so
%{_datadir}/pygtk/2.0/defs/metacity.defs

%if %{build_gnomeprint}
%files -n %{oname}-gnomeprint
%doc examples/gnomeprint/
%{py_platsitedir}/gtk-2.0/gnomeprint/
%{_datadir}/pygtk/2.0/defs/art.defs
%{_datadir}/pygtk/2.0/defs/print.defs
%{_datadir}/pygtk/2.0/defs/printui.defs
%{_datadir}/gtk-doc/html/pygnomeprint*
%endif

%if %{build_evince}
%files -n %{oname}-evince
%{py_platsitedir}/gtk-2.0/evince.so
%{_datadir}/pygtk/2.0/defs/evince.defs
%endif

%files -n %{oname}-wnck
%doc examples/wnck*
%{py_platsitedir}/gtk-2.0/wnck.so
%{_datadir}/pygtk/2.0/defs/wnck.defs

%files devel
%{_libdir}/pkgconfig/%{name}-2.0.pc

