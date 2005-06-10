%define		_decoration	dotcurve
Summary:	KDE Style - %{_decoration}
Summary(pl):	Styl do KDE - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Themes
#Source0Download: http://dotcurve.usefularts.org/download.html
Source0:	http://webs.ono.com/usr047/uucp/%{_decoration}-%{version}.tar.bz2
# Source0-md5:	fc9b655cd6689ad5055ccb781dde3848
URL:		http://kde-look.org/content/show.php?content=16211
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
Requires:	kdebase-desktop-libs >= 9:3.2.0
Obsoletes:	kde-decoration-dotcurve
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE style with flat widgets and rounded corners and striped
progressbar. 

%description -l pl
Ostre naro¿niki s± martwe (prawie). Niech ¿yj± okr±g³e! Szybki,
prosty, przejrzysty wygl±d. Zaleca siê u¿ywanie razem z dekoracj±
okien "Web".

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f /usr/share/automake/config.sub admin

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*
