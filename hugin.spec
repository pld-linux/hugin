Summary:	Toolchain to create panoramic images
Summary(pl):	Zestaw narz�dzi do tworzenia panoramicznych zdj��
Name:		hugin
Version:	0.6.1
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
# Source0-md5:	46bc3136d42acbabab837128ff471507
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-defaults.patch
Patch2:		%{name}-asneeded.patch
URL:		http://hugin.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-any-devel >= 1.31
BuildRequires:	boost-ref-devel >= 1.31
BuildRequires:	boost-test-devel >= 1.31
BuildRequires:	boost-bind-devel >= 1.31
BuildRequires:	boost-thread-devel >= 1.31
BuildRequires:	boost-uBLAS-devel >= 1.31
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpano12-devel >= 2.8.1
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires:	libpano12 >= 2.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With hugin you can assemble a mosaic of photographs into a complete
immensive panorama, stitch any series of overlapping pictures and much
more.

Note: Hugin can use autopano-sift package to match images and enblend
package for soft blending, so you'll probably want to install them
too.

%description -l pl
Przy u�yciu hugina mo�na po��czy� wiele fotografii w kompletn�, du��
panoram�, sklei� dowolny ci�g nak�adaj�cych si� zdj�� i wiele wi�cej.

Hugin mo�e u�ywa� pakietu autopano-sift do dopasowania zdj�� oraz
pakiet enblend do wyg�adzenia kraw�dzi po ��czeniu - wi�c warto te
pakiety tak�e zainstalowa�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's,/lib",/%{_lib}",' m4/ax_boost.m4
sed -i -e 's/ca_ES/ca/;s/cs_CZ/cs/;' src/hugin/po/LINGUAS
mv -f src/hugin/po/{ca_ES,ca}.po
mv -f src/hugin/po/{cs_CZ,cs}.po
# missing in LINGUAS
echo 'cs'>> src/nona_gui/po/LINGUAS
mv -f src/nona_gui/po/{cs_CZ,cs}.po

%build
%{__gettextize}
cp -f po/Makefile.in.in src/hugin/po
cp -f po/Makefile.in.in src/nona_gui/po
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-ansi-config
%{__make}

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
