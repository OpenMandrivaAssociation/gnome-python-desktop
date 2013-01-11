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
Release:	8
License:	LGPLv2+ and GPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
#gw link plparser wrapper with gtk until it was update for 2.29
Patch1:		gnome-python-desktop-2.29.1-totem-plparser-add-gtk.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=672016
Patch2:		gnome-python-desktop-2.32.0-metacity-build.patch
Patch3:		gnome-python-desktop-2.32.0-automake-1.13.patch

BuildRequires:	pygtk2.0-devel >= %pygtk
BuildRequires:	gnome-python-devel >= %gnomepython
BuildRequires:	gnome-python-gconf >= %gnomepython
BuildRequires:	python-devel >= 2.2
BuildRequires:	libgnomeui2-devel >= 2.0.0
BuildRequires:	gtksourceview1-devel >= 1.1.90
# let gotz keep all his gnome2 stuff intact in main
##BuildRequires: %{_lib}edataserver2-devel
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	libgnome-keyring-devel >= 0.5.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libcanberra-devel
BuildRequires:	x11-server-xvfb
#(tpg) do not require this :)
#Requires: gnome-desktop

Conflicts:	gnome-python-extras < 2.13.3

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
BuildRequires:	libgtop2.0-devel >= 2.13

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
Requires:	gnome-python-gconf >= %gnomepython
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
BuildRequires:	libgnomeprintui-devel >= 2.8.0

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
find %{buildroot} -name '*.la' -exec rm {} \;

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



%changelog
* Fri May 25 2012 Guilherme Moro <guilherme@mandriva.com> 2.32.0-7
+ Revision: 800748
- Drop evolution too
- Drop rsvg and applet
  fix for new metacity

* Mon Mar 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.32.0-6
+ Revision: 782181
- rebuild, disabling gtk3 ported apps, brasero, evince and mediaprofiles

* Mon Feb 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.32.0-5
+ Revision: 781162
- added in correct requires for individual pkgs
- removed nautilus-burn build
- split out devel, gnomekeyring, rsvg & wnck sub pkgs
- moved defs files to individual pkgs
- moved gnomedesktop files back to main pkg

* Sat Dec 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.32.0-4
+ Revision: 744981
- more clean ups to the spec and BRs
- rebuild
- disabled brasero build
- brasero needs to live in contrib now with tracker
- cleaned up spec

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 2.32.0-3
+ Revision: 652107
- link with libpython

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 591744
- rebuild for py 2.7

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581889
- new version
- drop patch 2

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 2.31.1-3mdv2011.0
+ Revision: 571610
- rebuild for new brasero

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 2.31.1-2mdv2011.0
+ Revision: 570982
- patch for new evince
- drop unapplied patch 0

* Tue Aug 10 2010 Götz Waschk <waschk@mandriva.org> 2.31.1-1mdv2011.0
+ Revision: 568296
- update to new version 2.31.1

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550822
- new version

* Tue Jun 22 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.0-2mdv2010.1
+ Revision: 548496
- rebuild with latest eds

  + Götz Waschk <waschk@mandriva.org>
    - bump evince dep

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529954
- update to new version 2.30.0

* Thu Mar 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 518050
- update to new version 2.29.92

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-3mdv2010.1
+ Revision: 497245
- fix build with new libtotem-plparser

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-2mdv2010.1
+ Revision: 490516
- rebuild for new libgnome-desktop

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 486193
- new version
- update build deps
- add brasero examples

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446699
- update to new version 2.28.0

* Tue Sep 01 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 423793
- new version
- disable the patch

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 396181
- new version
- update file list

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374198
- update deps
- new version
- add brasero module

* Sat Mar 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355147
- update to new version 2.26.0

* Thu Mar 12 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-2mdv2009.1
+ Revision: 354235
- disable nautilus-burn binding

  + Aleksey Lim <alsroot@mandriva.org>
    - Obsolete python-evince by gnome-python-evince

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340715
- update to new version 2.25.91

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-2mdv2009.1
+ Revision: 336802
- enable evince binding

* Sun Feb 01 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336227
- new version
- fix build
- update file list

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 330846
- New version 2.25.1

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 2.24.1-2mdv2009.1
+ Revision: 318756
- disable check (broken with python 2.6, see
  http://bugzilla.gnome.org/show_bug.cgi?id=565598 )
- rebuild for python 2.6

* Fri Dec 19 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 316351
- update deps
- fix build with the new panel
- new version
- run checks in xvfb

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-2mdv2009.1
+ Revision: 300181
- rebuild for new gnome-desktop

* Sun Sep 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286340
- new version

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 2.23.1-1mdv2009.0
+ Revision: 277971
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.0-1mdv2009.0
+ Revision: 231291
- new version
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183055
- new version

* Sun Feb 24 2008 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 174268
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 151944
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 120730
- new version
- add evolution binding
- fix buildrequires

* Thu Nov 01 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 104377
- rebuild for new totem

* Sun Sep 16 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 88471
- new version

* Tue Jul 31 2007 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 56911
- fix buildrequires
- new version
- fix buildrequires

* Sat Jul 07 2007 Götz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 49451
- new version
- drop patch

* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.18.0-2mdv2008.0
+ Revision: 41708
- needs gtksourceview 1 not 2
- add patch0 (from FreeBSD, fixes build against metacity 2.19)
- rebuild for new libwnck


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142017
- new version

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 2.17.93-1mdv2007.1
+ Revision: 126674
- new version
- drop the patch
- fix build

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-2mdv2007.1
+ Revision: 126481
- fix patch
- patch to support latest metacity
- reenable metacity
- new version
- drop patch
- disable metacity module for now
- fix build with new totem

* Mon Jan 08 2007 Götz Waschk <waschk@mandriva.org> 2.17.3-1mdv2007.1
+ Revision: 106025
- new version

* Mon Jan 08 2007 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 105441
- arrgh, bug-buddy module
- new version
- add gnucash module

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2007.1
+ Revision: 87808
- new version
- bump deps
- mkrel
- Import gnome-python-desktop

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New version 2.16.0

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- rebuild for new dbus

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- bump deps
- New release 2.15.90

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- New release 2.15.4

* Thu Jun 22 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-2mdv2007.0
- add gnome-keyring module

* Wed Jun 14 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2007.0
- bump deps
- New release 2.15.3

* Mon Jun 12 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-2mdv2007.0
- fix buildrequires

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-1mdv2007.0
- add gnomedesktop module
- New release 2.15.2
- add rsvg plugin

* Wed Apr 19 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-2mdk
- Rebuild

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- initial package split from gnome-python-extras

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 2.13.2-0.1gpw
- add metacity plugin

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 2.13.2-0.1gpw
- New release 2.13.2

* Mon Jan 02 2006 Götz Waschk <waschk@mandriva.org> 2.13.1-0.1gpw
- New release 2.13.1

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 2.13.0-0.3gpw
- add gksu support
- fix buildrequires

* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 2.13.0-0.2gpw
- fix gtksourceview deps (bug 18777)

* Mon Dec 12 2005 Götz Waschk <waschk@mandriva.org> 2.13.0-0.1gpw
- disable gda
- New release 2.13.0

* Sun Nov 20 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- rebuild for new openssl

* Mon Oct 31 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0
- add mediaprofiles package
- update file list
- requires new nautilus-burn
- regenerate configure
- rediff the patch
- enable gdl wrapper
- add pygda

* Mon May 30 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- rediff patches
- New release 2.10.2

* Wed May 18 2005 Götz Waschk <waschk@mandriva.org> 2.10.1-2mdk
- add gdl bindings
- patch for gcc4

* Sun Apr 24 2005 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- initial mdk version

* Tue Apr 12 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.1-0.1gpw
- patch configure, regeneration didn't work
- fix build
- New release 2.10.1

* Tue Mar 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-0.1gpw
- bump deps
- fix build for firefox
- New release 2.10.0

* Wed Feb 16 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.4-0.1gpw
- New release 2.9.4

* Wed Jan 26 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.3-0.2gpw
- add bindings for gtop, nautilus-burn and totem-plparser
- New release 2.9.3

* Sat Jan 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.2-0.2gpw
- rebuild for new howl

* Mon Jan 03 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.2-0.1gpw
- add mozembed and gtkspell modules
- New release 2.9.2

* Mon Dec 06 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.1-0.2gpw
- rebuild for new python

* Tue Nov 30 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.1-0.1gpw
- update file list

* Tue Nov 30 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.9.1-1mdk
- New release 2.9.1

* Mon Nov 22 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.0-0.1gpw
- initial package

