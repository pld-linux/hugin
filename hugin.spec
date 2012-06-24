Summary:	Toolchain to create panoramic images
Summary(pl):	Zestaw narz�dzi do tworzenia panoramicznych zdj��
Name:		hugin
Version:	0.5
%define	bver	rc2
Release:	0.%{bver}.1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}-%{bver}.tar.bz2
# Source0-md5:	632585f02c0ef34a6fda4ec7c231587d
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-defaults.patch
URL:		http://hugin.sf.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
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
BuildRequires:	libtool >= 2:1.5
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

sed -i -e 's,ac_boost_libdir=.*/lib.*,ac_boost_libdir=/usr/%{_lib},' m4/ax_check_boost.m4

# to rebuild pl.gmo
rm -f src/hugin/po/stamp-po

%build
%{__gettextize}
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
	DESTDIR=$RPM_BUILD_ROOT

# "hugin" and "nona_gui" domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog LICENCE_JHEAD LICENCE_VIGRA NEWS README TODO
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/nona_gui
%attr(755,root,root) %{_bindir}/zhang_undistort
%{_datadir}/%{name}
%{_datadir}/mime/packages/hugin.xml
%{_desktopdir}/hugin.desktop
%{_iconsdir}/gnome/*/mimetypes/*.png
%{_pixmapsdir}/hugin.png
