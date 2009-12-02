Summary:	Toolchain to create panoramic images
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia panoramicznych zdjęć
Name:		hugin
Version:	2009.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}.tar.gz
# Source0-md5:	856fa8016bc990874a71a19cc162f6be
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-asneeded.patch
Patch2:		%{name}-cppflags.patch
Patch3:		%{name}-boost-1.40-fix.patch
URL:		http://hugin.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	boost-devel >= 1.40.0
BuildRequires:	cmake >= 2.4
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel
BuildRequires:	glew-devel
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpano13-devel >= 2.9.12
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.471
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-unicode-devel >= 2.6.0
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.6.0
BuildRequires:	zip
BuildRequires:	zlib-devel
Suggests:	autopano-sift-C >= 2.5.0
Suggests:	enblend-enfuse >= 3.1
# exiftool program
Suggests:	perl-Image-ExifTool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With hugin you can assemble a mosaic of photographs into a complete
immensive panorama, stitch any series of overlapping pictures and much
more.

Note: Hugin can use autopano-sift-C package to match images and
enblend package for soft blending, so you'll probably want to install
them too.

%description -l pl.UTF-8
Przy użyciu hugina można połączyć wiele fotografii w kompletną, dużą
panoramę, skleić dowolny ciąg nakładających się zdjęć i wiele więcej.

Hugin może używać pakietu autopano-sift-C do dopasowania zdjęć oraz
pakiet enblend do wygładzenia krawędzi po łączeniu - więc warto te
pakiety także zainstalować.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

mv -f src/translations/{ca_ES,ca}.po
mv -f src/translations/{cs_CZ,cs}.po

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{?debug:Debug}%{!?debug:None} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-gtk2-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# cmake is so great there is no way to pass proper path
mv $RPM_BUILD_ROOT%{_iconsdir}/{gnome,hicolor}

# not needed
rm $RPM_BUILD_ROOT%{_libdir}/libhugin*.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENCE_VIGRA README TODO
%lang(ja) %doc README_JP
%attr(755,root,root) %{_bindir}/align_image_stack
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/autopano-noop.sh
%attr(755,root,root) %{_bindir}/celeste_standalone
%attr(755,root,root) %{_bindir}/fulla
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/hugin_hdrmerge
%attr(755,root,root) %{_bindir}/hugin_stitch_project
%attr(755,root,root) %{_bindir}/matchpoint
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/nona_gui
%attr(755,root,root) %{_bindir}/PTBatcher
%attr(755,root,root) %{_bindir}/PTBatcherGUI
%attr(755,root,root) %{_bindir}/pto2mk
%attr(755,root,root) %{_bindir}/tca_correct
%attr(755,root,root) %{_bindir}/vig_optimize
%attr(755,root,root) %{_libdir}/libceleste.so*
%attr(755,root,root) %{_libdir}/libhuginANN.so.*.*
%attr(755,root,root) %{_libdir}/libhuginbase.so.*.*
%attr(755,root,root) %{_libdir}/libhuginvigraimpex.so.*.*
%{_datadir}/%{name}
%{_datadir}/mime/packages/hugin.xml
%{_desktopdir}/hugin.desktop
%{_desktopdir}/PTBatcherGUI.desktop
%{_iconsdir}/hicolor/*/mimetypes/gnome-mime-application-x-ptoptimizer-script.png
%{_pixmapsdir}/hugin.png
%{_mandir}/man1/*
