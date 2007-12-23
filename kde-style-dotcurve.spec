%define		_decoration	dotcurve
Summary:	KDE Style - %{_decoration}
Summary(pl.UTF-8):	Styl do KDE - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0
%define _rc	rc1
Release:	0.%{_rc}.1
License:	LGPL
Group:		Themes
#Source0Download: http://dotcurve.usefularts.org/download.html
Source0:	http://webs.ono.com/uucp/dotcurve/files/%{_decoration}-%{version}%{_rc}.tar.bz2
# Source0-md5:	60ec9dfbc1b4cefcf02990c337591422
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

%description -l pl.UTF-8
Ostre narożniki są martwe (prawie). Niech żyją okrągłe! Szybki,
prosty, przejrzysty wygląd. Zaleca się używanie razem z dekoracją
okien "Web".

%prep
%setup -q -n %{_decoration}-%{version}%{_rc}

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
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kstyle/themes/*
