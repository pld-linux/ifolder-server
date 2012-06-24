# TODO
# - make use of libflaim-shared
Summary:	iFolder server
Summary(pl):	Serwer iFolder
Name:		ifolder3-server
Version:	3.5.6089.1
Release:	0.2
License:	GPL v2
Group:		Applications
Source0:	http://forgeftp.novell.com/ifolder/server/3.5/20060330-000/src/%{name}-%{version}.tar.gz
# Source0-md5:	ab69bc5fe3c27bbdd0f32b4ed056f130
URL:		http://www.ifolder.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libflaim-static
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Buildrequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	log4net
BuildRequires:	mono-compat-links
BuildRequires:	mono-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/ifolder3
%define		_libexecdir		%{_libdir}/ifolder3
%define		_simiasdatadir		/var/lib/ifolder3

%description
iFolder is a simple and secure storage solution that can increase your
productivity by enabling you to back up, access and manage your
personal files from anywhere, at anytime. Once you have installed
iFolder, you simply save your files locally as you have always done
and iFolder automatically updates the files on a network server and
delivers them to the other machines you use.

Sponsored by Novell, the iFolder project is built on the mono/.NET
framework to integrate seamlessly into existing desktop environments.

%description -l pl
iFolder to proste i bezpieczne rozwi�zanie przechowywania danych
zwi�kszaj�ce produktywno�� pozwalaj�c zapisywa�, odczytywa� i
zarz�dza� swoimi plikami z dowolnego miejsca w dowolnym czasie. Po
zainstalowaniu iFoldera wystarczy zapisywa� swoje pliki lokalnie, tak
jak zawsze, a iFolder automatycznie uaktualni pliki na serwerze
sieciowym i dostarczy je na inne u�ywane przez nas maszyny.

Projekt iFolder, sponsorowany przez Novella, jest stworzony w oparciu
o �rodowisko mono/.NET tak, aby integrowa� si� z istniej�cymi
�rodowiskami biurowymi.

%package devel
Summary:	Header files for simias library
Summary(pl):	Pliki nag��wkowe biblioteki simias
Group:		Development/Libraries

%description devel
This is the package containing the header files for simias library.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki simias.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-simiasdatadir=%{_simiasdatadir}

#  --with-ndoc-path=PATH        path to dir that contains NDocConsole.exe [NONE]
#  --with-client-setup     configure simias to run as a client. [Default=FALSE]
#  --with-pic              try to use only PIC/non-PIC objects [default=use both]

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use webapps (template-webapp.spec)
#ln -sf %{_sysconfdir}/simias_server.conf /etc/apache2/conf.d/simias_server.conf
#ln -sf %{_sysconfdir}/ifolder_admin.conf /etc/apache2/conf.d/ifolder_admin.conf
#ln -sf %{_sysconfdir}/ifolder_webaccess.conf /etc/apache2/conf.d/ifolder_webaccess.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/Simias.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/Simias.log4net
%dir %{_sysconfdir}/bill
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bill/Simias.config
%dir %{_sysconfdir}/bill/modules
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bill/modules/Simias.Server.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/defaults.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ifolder_admin.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ifolder_webaccess.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/simias_server.conf
%attr(755,root,root) %{_bindir}/SimiasDirectoryMapping
%attr(755,root,root) %{_bindir}/simias
%attr(755,root,root) %{_bindir}/simias-create-user
%attr(755,root,root) %{_bindir}/simias-delete-user
%attr(755,root,root) %{_bindir}/simias-user
%attr(755,root,root) %{_bindir}/simiasserver
%attr(755,root,root) %{_libdir}/libFlaimWrapper.so.*.*.*
%attr(755,root,root) %{_libdir}/libsimias-event.so.*.*.*
%attr(755,root,root) %{_libdir}/libsimias.so.*.*.*
%dir %{_libdir}/ifolder3
%{_libdir}/ifolder3/admin
%{_libdir}/ifolder3/bin
%{_libdir}/ifolder3/web
%{_libdir}/ifolder3/webaccess

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/simias
%{_includedir}/simias/simias-event-client.h
%{_includedir}/simias/simias-manager.h
%{_includedir}/simias/simias.h
%{_includedir}/simias/simias.nsmap
%{_includedir}/simias/simiasH.h
%{_includedir}/simias/simiasStub.h
%{_includedir}/simias/simiasweb.h
%{_includedir}/simias/stdsoap2.h
%{_pkgconfigdir}/simias-client-c.pc
%{_pkgconfigdir}/simias-client.pc
%{_pkgconfigdir}/simias.pc

#%{_libdir}/libsimias-manager.a
