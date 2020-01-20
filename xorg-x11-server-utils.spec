# doesn't work yet, needs more nickle bindings
%define with_xkeystone 0

# Component versions
%define iceauth 1.0.7
%define rgb 1.0.6
%define sessreg 1.1.0
%define xgamma 1.0.5
%define xhost 1.0.6
%define xinput 1.6.1
%define xkill 1.0.4
%define xmodmap 1.0.8
%define xrandr 1.4.3
%define xrdb 1.1.0
%define xrefresh 1.0.5
%define xset 1.2.3
%define xsetmode 1.0.0
%define xsetpointer 1.0.1
%define xsetroot 1.1.1
%define xstdcmap 1.0.3

Summary:    X.Org X11 X server utilities
Name:       xorg-x11-server-utils
Version:    7.7
Release:    14%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    http://www.x.org/pub/individual/app/iceauth-%{iceauth}.tar.bz2
Source1:    http://www.x.org/pub/individual/app/rgb-%{rgb}.tar.bz2
Source2:    http://www.x.org/pub/individual/app/sessreg-%{sessreg}.tar.bz2
Source3:    http://www.x.org/pub/individual/app/xgamma-%{xgamma}.tar.bz2
Source4:    http://www.x.org/pub/individual/app/xhost-%{xhost}.tar.bz2
Source5:    http://www.x.org/pub/individual/app/xinput-%{xinput}.tar.bz2
Source6:    http://www.x.org/pub/individual/app/xkill-%{xkill}.tar.bz2
Source7:    http://www.x.org/pub/individual/app/xmodmap-%{xmodmap}.tar.bz2
Source8:    http://www.x.org/pub/individual/app/xrandr-%{xrandr}.tar.bz2
Source9:    http://www.x.org/pub/individual/app/xrdb-%{xrdb}.tar.bz2
Source10:   http://www.x.org/pub/individual/app/xrefresh-%{xrefresh}.tar.bz2
Source11:   http://www.x.org/pub/individual/app/xset-%{xset}.tar.bz2
Source12:   http://www.x.org/pub/individual/app/xsetmode-%{xsetmode}.tar.bz2
Source13:   http://www.x.org/pub/individual/app/xsetpointer-%{xsetpointer}.tar.bz2
Source14:   http://www.x.org/pub/individual/app/xsetroot-%{xsetroot}.tar.bz2
Source15:   http://www.x.org/pub/individual/app/xstdcmap-%{xstdcmap}.tar.bz2

Patch2: 0001-Default-to-nocpp-add-cpp-default.patch

BuildRequires:  xorg-x11-util-macros

BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xxf86misc)
BuildRequires:  pkgconfig(xxf86vm)

BuildRequires:  libtool

Provides:   iceauth = %{iceauth}
Provides:   rgb = %{rgb}
Provides:   sessreg = %{sessreg}
Provides:   xgamma = %{xgamma}
Provides:   xhost = %{xhost}
Provides:   xinput = %{xinput}
Provides:   xkill = %{xkill}
Provides:   xmodmap = %{xmodmap}
Provides:   xrandr = %{xrandr}
Provides:   xrdb = %{xrdb}
Provides:   xrefresh = %{xrefresh}
Provides:   xset = %{xset}
Provides:   xsetmode = %{xsetmode}
Provides:   xsetpointer = %{xsetpointer}
Provides:   xsetroot = %{xsetroot}
Provides:   xstdcmap = %{xstdcmap}

%description
A collection of utilities used to tweak and query the runtime configuration of
the X server.

%if %{with_xkeystone}
%package -n xkeystone
Summary:    X display keystone correction
Requires:   nickle

%description -n xkeystone
Utility to perform keystone adjustments on X screens.
%endif

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15

pushd xrdb-*
%patch2 -p1 -b .nocpp
popd

%build

# Build all apps
{
   for app in * ; do
      pushd $app
      autoreconf -vif
      %configure
      make %{?_smp_mflags}
      popd
   done
}

%install
# Install all apps
{
   for app in * ; do
      pushd $app
      case $app in
         *)
            %make_install
            ;;
      esac
      popd
   done
}
%if !%{with_xkeystone}
rm -f $RPM_BUILD_ROOT%{_bindir}/xkeystone
%endif

%files
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
%{_bindir}/xkeystone
%endif

%changelog
* Mon Sep 07 2015 Olivier Fourdan <ofourdan@redhat.com> 7.7-14
- Fix regression introduced by the nocpp patch if no cpp is installed.

* Tue Jul 21 2015 Adam Jackson <ajax@redhat.com> 7.7-13
- Merge F22, rebase nocpp patch

* Tue Jan 20 2015 Simone Caronni <negativo17@gmail.com> - 7.7-12
- Update sessreg to 1.1.0.

* Sat Jan 17 2015 Simone Caronni <negativo17@gmail.com> - 7.7-11
- Update iceauth to 1.0.7.

* Mon Nov 10 2014 Simone Caronni <negativo17@gmail.com> - 7.7-10
- rgb 1.0.6

* Thu Oct 23 2014 Simone Caronni <negativo17@gmail.com> - 7.7-9
- Clean up SPEC file, fix rpmlint warnings.

* Wed Oct 01 2014 Adam Jackson <ajax@redhat.com> 7.7-8
- xrandr 1.4.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Simone Caronni <negativo17@gmail.com> 7.7-6
- iceauth 1.0.6
- xhost 1.0.6
- xrandr 1.4.2
- xrefresh 1.0.5
- xset 1.2.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Adam Jackson <ajax@redhat.com> 7.7-4.el7
- Fix configure to not point to mcpp either

* Mon Sep 16 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-4
- xinput 1.6.1

* Mon Sep 09 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-3
- xmodmap 1.0.8
- xkill 1.0.4
- xrdb 1.1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
