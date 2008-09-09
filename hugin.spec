#
# Conditional build:
%bcond_with	pano13			# use libpano13 instead of libpano12
#
%define		_beta	beta4
Summary:	Toolchain to create panoramic images
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia panoramicznych zdjęć
Name:		hugin
Version:	0.7.0
Release:	0.rc5.0.1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}_rc5.tar.gz
# Source0-md5:	cd99ce8985aec47b93e300c2be695680
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-asneeded.patch
Patch2:		%{name}-cppflags.patch
URL:		http://hugin.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libjpeg-devel
%{!?with_pano13:BuildRequires:	libpano12-devel >= 2.8.1}
%{?with_pano13:BuildRequires:	libpano13-devel}
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-unicode-devel >= 2.6.0
BuildRequires:	zip
BuildRequires:	zlib-devel
%{!?with_pano13:BuildConflicts:	libpano13-devel}
%{!?with_pano13:Requires:	libpano12 >= 2.8.1}
%{?with_pano13:Requires:	libpano13}
Suggests:	autopano-sift
Suggests:	enblend >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With hugin you can assemble a mosaic of photographs into a complete
immensive panorama, stitch any series of overlapping pictures and much
more.

Note: Hugin can use autopano-sift package to match images and enblend
package for soft blending, so you'll probably want to install them
too.

%description -l pl.UTF-8
Przy użyciu hugina można połączyć wiele fotografii w kompletną, dużą
panoramę, skleić dowolny ciąg nakładających się zdjęć i wiele więcej.

Hugin może używać pakietu autopano-sift do dopasowania zdjęć oraz
pakiet enblend do wygładzenia krawędzi po łączeniu - więc warto te
pakiety także zainstalować.

%prep
%setup -q 
# %%patch0 -p1
%patch1 -p1
%patch2

#sed -i -e 's/ca_ES/ca/;s/cs_CZ/cs/;' src/hugin/po/LINGUAS
mv -f src/translations/{ca_ES,ca}.po
mv -f src/translations/{cs_CZ,cs}.po
# missing in LINGUAS
# echo 'cs'>> src/nona_gui/po/LINGUAS

%build
install -d build
cd build

export CPPFLAGS="%{rpmcppflags}"  
%cmake \
	-DCMAKE_BUILD_TYPE:STRING="None" \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-gtk2-ansi-config \
	..
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemimeicondir=%{_iconsdir}/hicolor/48x48/mimetypes

# "hugin" and "nona_gui" domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog LICENCE_JHEAD LICENCE_VIGRA NEWS README TODO
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/color_correct_tiff
%attr(755,root,root) %{_bindir}/fulla
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/nona_gui
%attr(755,root,root) %{_bindir}/zhang_undistort
%{_datadir}/%{name}
%{_datadir}/mime/packages/hugin.xml
%{_desktopdir}/hugin.desktop
%{_iconsdir}/hicolor/*/mimetypes/*.png
%{_pixmapsdir}/hugin.png
%{_mandir}/man1/fulla.1*
