Summary:	Toolchain to create panoramic images
Summary(pl):	Zestaw narz�dzi do tworzenia panoramicznych zdj��
Name:		hugin
Version:	0.5
%define	bver	beta4
Release:	0.%{bver}.3
# SIFT is patented in USA and may require license for commercial use
License:	GPL, non-commercial SIFT license for some code
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}-%{bver}.tar.bz2
# Source0-md5:	b852b334400ba9d4ae91a5a628846491
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-defaults.patch
URL:		http://hugin.sf.net/
BuildRequires:	boost-any-devel
BuildRequires:	boost-ref-devel
BuildRequires:	boost-test-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpano12-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRequires:	zlib-devel
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

Hugin mo�e u�ywa� pakietu autopano-shift do dopasowania zdj�� oraz
pakiet enblend do wyg�adzenia kraw�dzi po ��czeniu - wi�c warto te
pakiety tak�e zainstalowa�.

%prep
%setup -q -n %{name}-%{version}-%{bver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's,ac_boost_libdir=.*/lib.*,ac_boost_libdir=/usr/%{_lib},' configure

%build
%configure \
	--with-wx-config=wx-gtk2-ansi-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# "hugin" and "nona_gui" domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog LICENCE_SIFT README TODO
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/nona_gui
%attr(755,root,root) %{_bindir}/panosifter
%attr(755,root,root) %{_bindir}/sift_keypoints
%attr(755,root,root) %{_bindir}/zhang_undistort
%{_datadir}/%{name}
