%define pkgname server-utils
# doesn't work yet, needs more nickle bindings
%define with_xkeystone 0

Summary: X.Org X11 X server utilities
Name: xorg-x11-%{pkgname}
Version: 7.7
Release: 14%{?dist}
License: MIT
Group: User Interface/X
URL: http://www.x.org

Source0:  http://www.x.org/pub/individual/app/iceauth-1.0.7.tar.bz2
Source2:  http://www.x.org/pub/individual/app/rgb-1.0.6.tar.bz2
Source3:  http://www.x.org/pub/individual/app/sessreg-1.1.0.tar.bz2
Source5:  http://www.x.org/pub/individual/app/xgamma-1.0.5.tar.bz2
Source6:  http://www.x.org/pub/individual/app/xhost-1.0.6.tar.bz2
Source7:  http://www.x.org/pub/individual/app/xmodmap-1.0.8.tar.bz2
Source8:  http://www.x.org/pub/individual/app/xrandr-1.4.3.tar.bz2
Source9:  http://www.x.org/pub/individual/app/xrdb-1.1.0.tar.bz2
Source10: http://www.x.org/pub/individual/app/xrefresh-1.0.5.tar.bz2
Source11: http://www.x.org/pub/individual/app/xset-1.2.3.tar.bz2
Source12: http://www.x.org/pub/individual/app/xsetmode-1.0.0.tar.bz2
Source13: http://www.x.org/pub/individual/app/xsetpointer-1.0.1.tar.bz2
Source14: http://www.x.org/pub/individual/app/xsetroot-1.1.1.tar.bz2
Source15: http://www.x.org/pub/individual/app/xstdcmap-1.0.3.tar.bz2
Source16: http://www.x.org/pub/individual/app/xkill-1.0.4.tar.bz2
Source17: http://www.x.org/pub/individual/app/xinput-1.6.1.tar.bz2

BuildRequires: xorg-x11-util-macros

BuildRequires: pkgconfig(xmu) pkgconfig(xext) pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm) pkgconfig(xrender) pkgconfig(xi)
BuildRequires: pkgconfig(xt) pkgconfig(xpm) pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(xproto) >= 7.0.25
# xsetroot requires xbitmaps-devel (which was renamed now)
BuildRequires: xorg-x11-xbitmaps
# xsetroot
BuildRequires: libXcursor-devel
# xinput
BuildRequires: libXinerama-devel

BuildRequires: autoconf automake libtool

# xrdb, sigh
Requires: mcpp
# older -apps had xinput and xkill, moved them here because they're
# a) universally useful and b) don't require Xaw
Conflicts: xorg-x11-apps < 7.6-4

Provides: iceauth rgb sessreg xgamma xhost
Provides: xmodmap xrandr xrdb xrefresh xset xsetmode xsetpointer
Provides: xsetroot xstdcmap xinput xkill

%description
A collection of utilities used to tweak and query the runtime configuration
of the X server.

%if %{with_xkeystone}
%package -n xkeystone
Summary: X display keystone correction
Group: User Interface/X
Requires: nickle

%description -n xkeystone
Utility to perform keystone adjustments on X screens.
%endif

%prep
%setup -q -c %{name}-%{version} -a2 -a3 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17

%build

# Build all apps
{
   for app in * ; do
      pushd $app
      case $app in
         rgb-*)
            autoreconf -vif
            %configure ;# --with-rgb-db=%{_datadir}/X11
            ;;
	 xset-*)
            autoreconf -vif
	    %configure
	    ;;
         *)
            autoreconf -vif
            %configure --with-cpp=/usr/bin/mcpp
            ;;
      esac

      make
      popd
   done
}

%install
rm -rf $RPM_BUILD_ROOT
# Install all apps
{
   for app in * ; do
      pushd $app
      case $app in
         *)
            make install DESTDIR=$RPM_BUILD_ROOT
            ;;
      esac
      popd
   done
}
%if !%{with_xkeystone}
rm -f $RPM_BUILD_ROOT/usr/bin/xkeystone
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/iceauth
%{_bindir}/sessreg
%{_bindir}/showrgb
%{_bindir}/xgamma
%{_bindir}/xhost
%{_bindir}/xinput
%{_bindir}/xkill
%{_bindir}/xmodmap
%{_bindir}/xrandr
%{_bindir}/xrdb
%{_bindir}/xrefresh
%{_bindir}/xset
%{_bindir}/xsetmode
%{_bindir}/xsetpointer
%{_bindir}/xsetroot
%{_bindir}/xstdcmap
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/sessreg.1*
%{_mandir}/man1/showrgb.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinput.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xmodmap.1*
%{_mandir}/man1/xrandr.1*
%{_mandir}/man1/xrdb.1*
%{_mandir}/man1/xrefresh.1*
%{_mandir}/man1/xset.1*
%{_mandir}/man1/xsetmode.1*
%{_mandir}/man1/xsetpointer.1*
%{_mandir}/man1/xsetroot.1*
%{_mandir}/man1/xstdcmap.1*

%if %{with_xkeystone}
%files -n xkeystone
%defattr(-,root,root,-)
%{_bindir}/xkeystone
%endif

%changelog
* Tue Nov 03 2015 Adam Jackson <ajax@redhat.com> 7.7-14
- Sync sources with RHEL 7.2, drop merged patches

* Fri Jun 13 2014 Adam Jackson <ajax@redhat.com> 7.7-2
- Fix utmp sessreg usage (#978523)

* Wed Mar 27 2013 Adam Jackson <ajax@redhat.com> 7.7-1
- rgb 1.0.5
- xsessreg 1.0.8
- xgamma 1.0.5
- xhost 1.0.5
- xmodmap 1.0.7
- xsetroot 1.1.1
- xstdcmap 1.0.3

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 7.5-17
- autoconf for aarch64

* Wed Feb 13 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 7.5-16
- xrandr 1.4.0

* Wed Jan 30 2013 Adam Jackson <ajax@redhat.com> 7.5-15
- Print primary output in xrandr

* Wed Nov 14 2012 Adam Jackson <ajax@redhat.com> 7.5-14
- xinput 1.6.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.5-12
- Add libXinerama-devel requires for new xinput

* Tue Apr 17 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.5-11
- xinput 1.5.99.901

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-9
- xinput 1.5.4

* Thu Nov 10 2011 Adam Jackson <ajax@redhat.com> 7.5-8
- Move xinput and xkill here from xorg-x11-apps

* Mon Oct 10 2011 Matěj Cepl <mcepl@redhat.com> - 7.5-7
- Fix BuildRequires ... xbitmaps-devel does not exist anymore (RHBZ #744751)
- Upgrade to the latest upstream iceauth, rgb, sessreg, and xrandr
