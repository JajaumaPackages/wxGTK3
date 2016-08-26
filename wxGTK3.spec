%global srcname wxWidgets
%global wxgtkname wxGTK3
%global wxbasename wxBase3
#RHEL 6 does not have gtk3
#RHEL prior to 6 is unsupported by this package
%if 0%{?el6}
%global gtkver 2
%else
%global gtkver 3
%endif

Name:           %{wxgtkname}
Version:        3.0.2
Release:        19%{?dist}
Summary:        GTK port of the wxWidgets GUI library
License:        wxWidgets
Group:          System Environment/Libraries
URL:            http://www.wxwidgets.org/
Source0:        http://downloads.sf.net/wxwindows/%{srcname}-%{version}.tar.bz2
Source1:        http://downloads.sf.net/wxwindows/%{srcname}-%{version}-docs-html.tar.bz2
Source10:       wx-config
# https://bugzilla.redhat.com/show_bug.cgi?id=1225148
# remove abort when ABI check fails
# Backport from wxGTK
Patch0:         %{name}-%{version}-abicheck.patch
# This is a collection of fixes from upstream
# to fix warnings and crashes. See bug for details:
# https://bugzilla.redhat.com/show_bug.cgi?id=1234211
Patch1:         %{name}-%{version}-upstreamfixes.patch
# This fixes the spinbutton on gtk 3.12+
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/312ae4c92cec95954557347c2b7a9e24d4398a59
Patch2:         %{name}-%{version}-spibuttfix.patch
# This fixes checkbox/radiobutton on gtk 3.14+
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/c1d150ed1228c155054cf1fa90932ced7371e6a4
Patch3:         %{name}-%{version}-checkradio.patch
# This fixes some wayland issues with GTK3
# For more details, see the upstream bug:
# http://trac.wxwidgets.org/ticket/16688
Patch4:         %{name}-%{version}-wayland.patch
# This fixes wxSTC compilation with GCC6
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/73e9e18ea09ffffcaac50237def0d9728a213c02
Patch5:         %{name}-%{version}-stc-gcc6.patch
# This fixes compilation of the strings tests with GCC6
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/01f62c02957cc1443ea761ddffe0b4322d987a1d
Patch6:         %{name}-%{version}-string-tests-gcc6.patch
# This prevents wxStaticText from widening each time SetLabel() is called
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/2bc3721f065fd7d47674ccaf7e8d9d6cc195aab5
Patch7:         %{name}-%{version}-getbestsize.patch
# These patches fix top level window sizing under Wayland
# For more details, see the upstream commits:
# https://github.com/wxWidgets/wxWidgets/commit/41be4271e18a21acbcc30d1e61653190f8ef7a6d
# https://github.com/wxWidgets/wxWidgets/commit/0388ce8e25535415d9bdd79ce14eb20e73859279
Patch8:         %{name}-%{version}-wayland-window-sizing1.patch
Patch9:         %{name}-%{version}-wayland-window-sizing2.patch
# This patch adds docs for the wxEVT_MEDIA_XXX event types (for Phoenix)
# For more details, see the upstream commits:
# https://github.com/wxWidgets/wxWidgets/commit/03903c1e459f108e0c464db24064e4cde84f174a
Patch10:        %{name}-%{version}-media-docs.patch
# Fixes issue with size allocation in GTK 3.19+
# For more details, see the upstream commit:
# https://github.com/wxWidgets/wxWidgets/commit/9fea81c069f9d803d79c4ce82f87a00a6e10b490
Patch11:	%{name}-%{version}-size-alloc-fix.patch

BuildRequires:  gtk%{gtkver}-devel
#Note webkitgtk (GTK2) does not appear to be supported
%if %{gtkver} == 3
BuildRequires:  webkitgtk3-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  expat-devel
BuildRequires:  SDL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  cppunit-devel
BuildRequires:  libmspack-devel
BuildRequires:  doxygen

Provides:       %{srcname} = %{version}-%{release}
Provides:       bundled(scintilla) = 3.2.1
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}

%description
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        devel
Group:          Development/Libraries
Summary:        Development files for the wxGTK3 library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl = %{version}-%{release}
Requires:       %{name}-media = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       gtk%{gtkver}-devel
Requires:       libGLU-devel
Provides:       %{srcname}-devel = %{version}-%{release}

%description devel
This package include files needed to link with the wxGTK3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        gl
Summary:        OpenGL add-on for the wxWidgets library
Group:          System Environment/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        media
Summary:        Multimedia add-on for the wxWidgets library
Group:          System Environment/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxbasename}
Summary:        Non-GUI support classes from the wxWidgets library
Group:          System Environment/Libraries

%description -n %{wxbasename}
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.


%package        docs
Group:          Development/Libraries
Summary:        Documentation for the wxGTK3 library
Requires:       %{name} = %{version}-%{release}
Provides:       %{srcname}-docs = %{version}-%{release}
BuildArch:      noarch

%description docs
This package provides documentation for the %{srcname} library.


%package        xmldocs
Group:          Development/Libraries
Summary:        XML Documentation for the wxGTK3 library
Requires:       %{name} = %{version}-%{release}
Provides:       %{srcname}-xmldocs = %{version}-%{release}
BuildArch:      noarch

%description xmldocs
This package provides XML documentation for the %{srcname} library.


%prep
%setup -q -n %{srcname}-%{version} -a 1
%patch0 -p1 -b .abicheck
%patch1 -p1 -b .upstreamfixes
%patch2 -p1 -b .spinbutt
%patch3 -p1 -b .checkradio
%patch4 -p1 -b .wayland
%patch5 -p1 -b .stc-gcc6
%patch6 -p1 -b .strings-tests-gcc6
%patch7 -p1 -b .getbestsize
%patch8 -p1 -b .wayland-window-sizing1
%patch9 -p1 -b .wayland-window-sizing2
%patch10 -p1 -b .media-docs
%patch11 -p1 -b .size-alloc-fix

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin3.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd3.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw3.mo|' Makefile.in

# rename docs directory
mv %{srcname}-%{version} html


# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|%{_libdir}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

# Trick configure into using pkg-config for cppunit-config
sed -i -e 's|$CPPUNIT_CONFIG --version|$CPPUNIT_CONFIG --modversion|' configure


%build
# likely still dereferences type-punned pointers
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# fix unused-direct-shlib-dependency error:
export LDFLAGS="-Wl,--as-needed"
# Trick configure into using pkg-config for cppunit-config
export CPPUNIT_CONFIG="/usr/bin/pkg-config cppunit"

%configure \
  --with-gtk=%{gtkver} \
  --with-opengl \
  --with-sdl \
  --with-gnomeprint \
  --with-libmspack \
  --enable-intl \
  --enable-no_deps \
  --disable-rpath \
  --enable-ipv6

make %{?_smp_mflags}

pushd docs/doxygen
WX_SKIP_DOXYGEN_VERSION_CHECK=1 ./regen.sh xml
popd

%install
%makeinstall

# install our multilib-aware wrapper
##Remove installed
rm %{buildroot}%{_bindir}/wx-config
##Install new and symlink
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_libexecdir}/%{name}/wx-config
ln -s ../..%{_libexecdir}/%{name}/wx-config %{buildroot}%{_bindir}/wx-config-3.0
##If gtk2
%if %{gtkver} == 2
sed -i -e 's|gtk3|gtk2|' %{buildroot}%{_libexecdir}/%{name}/wx-config
%endif

#Move wxrc to libexec and symlink (avoid conflict with wxGTK)
mv %{buildroot}%{_bindir}/wxrc* %{buildroot}%{_libexecdir}/%{name}
ln -s ../..%{_libexecdir}/%{name}/wxrc-3.0 %{buildroot}%{_bindir}/wxrc-3.0

# move bakefiles to avoid conflicts with 2.8.*
mkdir %{buildroot}%{_datadir}/bakefile/presets/wx3
mv %{buildroot}%{_datadir}/bakefile/presets/*.* %{buildroot}%{_datadir}/bakefile/presets/wx3

%find_lang wxstd3
%find_lang wxmsw3
cat wxmsw3.lang >> wxstd3.lang

%check
pushd tests
make %{?_smp_mflags} test
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gl -p /sbin/ldconfig
%postun gl -p /sbin/ldconfig

%post media -p /sbin/ldconfig
%postun media -p /sbin/ldconfig

%post -n %{wxbasename} -p /sbin/ldconfig
%postun -n %{wxbasename} -p /sbin/ldconfig

%files -f wxstd3.lang
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%{_libdir}/libwx_gtk%{gtkver}u_adv-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_aui-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_core-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_html-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_propgrid-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_qa-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_ribbon-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_richtext-*.so.*
%{_libdir}/libwx_gtk%{gtkver}u_stc-*.so.*
%if %{gtkver} == 3
%{_libdir}/libwx_gtk%{gtkver}u_webview-*.so.*
%endif
%{_libdir}/libwx_gtk%{gtkver}u_xrc-*.so.*

%files devel
%{_bindir}/wxrc-3.0
%{_bindir}/wx-config-3.0
%{_includedir}/wx-3.0
%{_libdir}/libwx_*.so
%{_libdir}/wx
%{_datadir}/aclocal/wxwin3.m4
%{_datadir}/bakefile/presets/wx3
#Exclude some python bitecode
%exclude %{_datadir}/bakefile/presets/wx3/*.pyc
%exclude %{_datadir}/bakefile/presets/wx3/*.pyo
%{_libexecdir}/%{name}

%files gl
%{_libdir}/libwx_gtk%{gtkver}u_gl-*.so.*

%files media
%{_libdir}/libwx_gtk%{gtkver}u_media-*.so.*

%files -n %{wxbasename}
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%{_libdir}/libwx_baseu-*.so.*
%{_libdir}/libwx_baseu_net-*.so.*
%{_libdir}/libwx_baseu_xml-*.so.*

%files docs
%doc html

%files xmldocs
%doc docs/doxygen/out/xml/*

%changelog
* Mon Apr  4 2016 Tom Callaway <tcallawa@redhat.com> - 3.0.2-19
- Add patch to resolve window sizing issue with gtk 3.19+

* Sun Mar 20 2016 Scott Talbert <swt@techie.net> - 3.0.2-18
- Add patch for wxEVT_MEDIA_XXX event types (for Phoenix)

* Wed Feb 24 2016 Scott Talbert <swt@techie.net> - 3.0.2-17
- Add patch to resolve issue with wxStaticText growing, fixes RH#1282142
- Add patches to resolve issues under Wayland with window sizing, RH#1294229

* Tue Feb 23 2016 Scott Talbert <swt@techie.net> - 3.0.2-16
- Add -xmldocs subpackage containing XML documentation (needed for Phoenix)

* Tue Feb 23 2016 Scott Talbert <swt@techie.net> - 3.0.2-15
- Add GCC6 patches for STC and strings tests
- Adapt cppunit to use pkg-config (cppunit-config has been removed in F24)
- Fixes FTBFS in F24 Rawhide, RH#1308244

* Mon Feb 22 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-14
- Should actually fix RH#1294712

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-12
- Remove python artifacts in bakefile dir, causes multilib devel conflict RH#1294712
- Fix package devel not owning created wx3 backfile preset dir
- Add support for MIPS to wx-config RH#1294895
- Wayland Patch

* Thu Nov 5 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-11
- Added patch to fix checkbox and radio button issues for f21 onwards

* Sun Nov 1 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-10
- Removed depreciated/retired libgnomeprintui22

* Sat Aug 22 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-9
- Include spinbutton patch from upstream

* Mon Jun 22 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-8
- Include some upstream patches to fix crashes and warnings

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-6
- Don't abort on ABI check, backport from wxGTK

* Mon May 04 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.0.2-5
- Indicate that this package bundles scintilla 3.2.1.

* Thu Feb 26 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-4
- Bump to rebuild, fix bug #1210239

* Thu Feb 26 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-3
- Bump to rebuild for gcc 5.0 to fix some issues

* Tue Nov 04 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-2
- Moving things around again, hopefully fixing RH#1124402
- Adding symlinks to avoid breaking things

* Tue Nov 04 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-1
- Update to 3.0.2

* Mon Nov 03 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 3.0.1-5
- Add aarch64 and ppc64le to list of 64-bit architectures

* Tue Sep 30 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-4
- Add conflict with wxgtk-devel again, temporary fix until it can be resolved

* Tue Sep 30 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-3
- Avoid gtk warnings, fixes RH#1147995
- Moving wxrc and wx-config to libexec instead of renaming
- Misc changes and spec error fixes, fixes RH#1124402

* Sat Jul 5 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-1
- Bump to 3.0.1 RH#1076617

* Tue Mar 18 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-6
- Removed disable-catch_segvs, see RH#1076617

* Mon Mar 17 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-5
- Renable combat28 - without it causes bugs RH#1076617 and a few others

* Wed Feb 19 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-4
- Fixed GTK3 bug with wx-config
- Fixed a unused-direct-shlib-dependency error

* Mon Feb 17 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-3
- Added patch to avoid build fail on gtk 3.10+
- Reverted patching to make devel package compatible with wxGTK-devel
- Added combatibility for RHEL 6+
- Changed all mention of GTK3 and GTK2 to GTK for consistency

* Mon Feb 10 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-2
- Changed to build against gtk3
- Add webkit to build requires
- Removed patching to make devel package compatible with wxGTK-devel
- Disable 2.8.* combatibility (redundant functionality)

* Sat Jan 4 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-1
- Initial build of wxwidgets version 3, mostly based on wxGTK spec
