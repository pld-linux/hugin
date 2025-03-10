Summary:	Toolchain to create panoramic images
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia panoramicznych zdjęć
Name:		hugin
Version:	2024.0.1
Release:	3
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
# Source0-md5:	7e8ce50af10ace1a900e097ece206123
URL:		https://hugin.sourceforge.io/
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	ZThread-devel
BuildRequires:	boost-devel >= 1.47.0
BuildRequires:	cmake >= 3.8
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-devel >= 3
BuildRequires:	flann-devel >= 1.9.2-4
BuildRequires:	gettext-tools
BuildRequires:	glew-devel
BuildRequires:	gtk+3-devel
BuildRequires:	lcms2-devel >= 2
BuildRequires:	lensfun-devel
BuildRequires:	libgomp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpano13-devel >= 2.9.19
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl-Image-ExifTool
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	swig-python >= 2.0.4
BuildRequires:	tclap
BuildRequires:	vigra-devel >= 1.11.1-14
BuildRequires:	wxGTK3-unicode-devel >= 2.8.10
BuildRequires:	wxGTK3-unicode-gl-devel >= 2.8.10
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	libpano13 >= 2.9.19
Requires:	wxGTK3-unicode >= 2.8.10
Requires:	wxGTK3-unicode-gl >= 2.8.10
Suggests:	enblend-enfuse >= 3.1
# exiftool program
Suggests:	perl-Image-ExifTool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With hugin you can assemble a mosaic of photographs into a complete
immensive panorama, stitch any series of overlapping pictures and much
more.

Note: Hugin can use enblend and enfuse for soft blending/fusing, so
you'll probably to install enblend-enfuse package too.

%description -l pl.UTF-8
Przy użyciu hugina można połączyć wiele fotografii w kompletną, dużą
panoramę, skleić dowolny ciąg nakładających się zdjęć i wiele więcej.

Hugin może używać programów enblend i enfuse do wygładzania krawędzi i
ekspozycji, więc warto zainstalować pakiet enblend-enfuse.

%prep
%setup -q

# Old, broken duplicate of the system cmake one
%{__rm} CMakeModules/FindZLIB.cmake

%{__mv} src/translations/{cs_CZ,cs}.po

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	src/hugin_script_interface/hpi.py \
	src/hugin_script_interface/plugins/top_five.py \
	src/hugin_script_interface/plugins/woa.py \
	src/hugin_script_interface/plugins-dev/dual_use.py \
	src/hugin_script_interface/plugins-dev/plugin_skeleton.py

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DBUILD_HSI:BOOL=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk3-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ca_ES,ca}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ca_ES@valencia,ca@valencia}

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS Changes.txt README TODO src/celeste/LICENCE_{GABOR,LIBSVM}
%attr(755,root,root) %{_bindir}/PTBatcherGUI
%attr(755,root,root) %{_bindir}/align_image_stack
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/calibrate_lens_gui
%attr(755,root,root) %{_bindir}/celeste_standalone
%attr(755,root,root) %{_bindir}/checkpto
%attr(755,root,root) %{_bindir}/cpclean
%attr(755,root,root) %{_bindir}/cpfind
%attr(755,root,root) %{_bindir}/deghosting_mask
%attr(755,root,root) %{_bindir}/fulla
%attr(755,root,root) %{_bindir}/geocpset
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/hugin_executor
%attr(755,root,root) %{_bindir}/hugin_hdrmerge
%attr(755,root,root) %{_bindir}/hugin_lensdb
%attr(755,root,root) %{_bindir}/hugin_stacker
%attr(755,root,root) %{_bindir}/hugin_stitch_project
%attr(755,root,root) %{_bindir}/icpfind
%attr(755,root,root) %{_bindir}/linefind
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/pano_modify
%attr(755,root,root) %{_bindir}/pano_trafo
%attr(755,root,root) %{_bindir}/pto_gen
%attr(755,root,root) %{_bindir}/pto_lensstack
%attr(755,root,root) %{_bindir}/pto_mask
%attr(755,root,root) %{_bindir}/pto_merge
%attr(755,root,root) %{_bindir}/pto_move
%attr(755,root,root) %{_bindir}/pto_template
%attr(755,root,root) %{_bindir}/pto_var
%attr(755,root,root) %{_bindir}/tca_correct
%attr(755,root,root) %{_bindir}/verdandi
%attr(755,root,root) %{_bindir}/vig_optimize
%dir %{_libdir}/hugin
%attr(755,root,root) %{_libdir}/hugin/libceleste.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginbase.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginbasewx.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libicpfindlib.so.*.*
%attr(755,root,root) %{_libdir}/hugin/liblocalfeatures.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhugin_python_interface.so.*.*
%attr(755,root,root) %{py3_sitedir}/_hsi.so
%{py3_sitedir}/hpi.py*
%{py3_sitedir}/hsi.py*
%{py3_sitedir}/__pycache__/hpi.cpython-*.py[co]
%{py3_sitedir}/__pycache__/hsi.cpython-*.py[co]
%{_datadir}/%{name}
%{_datadir}/metainfo/PTBatcherGUI.appdata.xml
%{_datadir}/metainfo/calibrate_lens_gui.appdata.xml
%{_datadir}/metainfo/hugin.appdata.xml
%{_datadir}/mime/packages/hugin.xml
%{_desktopdir}/hugin.desktop
%{_desktopdir}/pto_gen.desktop
%{_desktopdir}/PTBatcherGUI.desktop
%{_desktopdir}/calibrate_lens_gui.desktop
%{_iconsdir}/hicolor/*x*/apps/hugin.png
%{_iconsdir}/hicolor/*x*/apps/ptbatcher.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-ptoptimizer-script.png
%{_iconsdir}/hicolor/scalable/apps/hugin.svg
%{_iconsdir}/hicolor/scalable/apps/ptbatcher.svg
%{_mandir}/man1/PTBatcherGUI.1*
%{_mandir}/man1/align_image_stack.1*
%{_mandir}/man1/autooptimiser.1*
%{_mandir}/man1/calibrate_lens_gui.1*
%{_mandir}/man1/celeste_standalone.1*
%{_mandir}/man1/checkpto.1*
%{_mandir}/man1/cpclean.1*
%{_mandir}/man1/cpfind.1*
%{_mandir}/man1/deghosting_mask.1*
%{_mandir}/man1/fulla.1*
%{_mandir}/man1/geocpset.1*
%{_mandir}/man1/hugin.1*
%{_mandir}/man1/hugin_executor.1*
%{_mandir}/man1/hugin_hdrmerge.1*
%{_mandir}/man1/hugin_lensdb.1*
%{_mandir}/man1/hugin_stacker.1*
%{_mandir}/man1/hugin_stitch_project.1*
%{_mandir}/man1/icpfind.1*
%{_mandir}/man1/linefind.1*
%{_mandir}/man1/nona.1*
%{_mandir}/man1/pano_modify.1*
%{_mandir}/man1/pano_trafo.1*
%{_mandir}/man1/pto_gen.1*
%{_mandir}/man1/pto_lensstack.1*
%{_mandir}/man1/pto_merge.1*
%{_mandir}/man1/pto_mask.1*
%{_mandir}/man1/pto_move.1*
%{_mandir}/man1/pto_template.1*
%{_mandir}/man1/pto_var.1*
%{_mandir}/man1/tca_correct.1*
%{_mandir}/man1/vig_optimize.1*
%{_mandir}/man1/verdandi.1*
