#
# Conditional build:
#%bcond_with	tests		# build with tests
#%bcond_without	tests		# build without tests
#
%define sysconfdir /etc/ifolder3
%define libexecdir /usr/lib/ifolder3
%define simiasdatadir /var/lib/ifolder3

Summary:	Server IFolder
Summary(pl):	Server IFolder
Name:		ifolder3-server
Version:	3.5.6089.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://forgeftp.novell.com/ifolder/server/3.5/20060330-000/src/%{name}-%{version}.tar.gz
# Source0-md5:	ab69bc5fe3c27bbdd0f32b4ed056f130
URL:		http://www.ifolder.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	libstdc++-devel
BuildRequires:	libstdc++
BuildRequires:	compat-libstdc++-3.1
BuildRequires:	gcc-c++
BuildRequires:	mono
BuildRequires:	mono-devel
BuildRequires:	mono-compat-links
BuildRequires:	pkgconfig
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	log4net-devel
BuildRequires:	libflaim-devel
Requires(post,preun):	/sbin/chkconfig
#Requires:	mono-core >= 1.1.8
#Requires:	mono-data >= 1.1.8
#Requires:	mono-web >= 1.1.8
#Requires:	log4net
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

iFolder is a simple and secure storage solution that can increase your
productivity by enabling you to back up, access and manage your
personal files¿from anywhere, at anytime. Once you have installed
iFolder, you simply save your files locally¿as you have always
done¿and iFolder automatically updates the files on a network server
and delivers them to the other machines you use.

Sponsored by Novell, the iFolder project is built on the mono/.Net
framework to integrate seamlessly into existing desktop environments

%description -l pl

%package libs
Summary:	-
Summary(pl):	-
Group:		Libraries

%description libs

%description libs -l pl


%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

%prep
%setup -q
#%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# remove svn control files
find -name .svn -print0 | xargs -0 rm -rf

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

#cp -f /usr/share/automake/config.sub .
#./autogen.sh
%configure	--libexecdir=%{libexecdir} \
		--sysconfdir=%{sysconfdir} \
		--with-simiasdatadir=%{simiasdatadir}
#  --with-ndoc-path=PATH        path to dir that contains NDocConsole.exe [NONE]
#  --with-client-setup     configure simias to run as a client. [Default=FALSE]
#  --with-pic              try to use only PIC/non-PIC objects [default=use both]
%{__make}
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
ln -sf %{sysconfdir}/simias_server.conf /etc/apache2/conf.d/simias_server.conf
ln -sf %{sysconfdir}/ifolder_admin.conf /etc/apache2/conf.d/ifolder_admin.conf
ln -sf %{sysconfdir}/ifolder_webaccess.conf /etc/apache2/conf.d/ifolder_webaccess.conf


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != %{_sysconfdir}:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
