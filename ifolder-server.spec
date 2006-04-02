Summary:	Server IFolder
Summary(pl):	Server IFolder
Name:		ifolder3-server
Version:	3.5.6089.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://forgeftp.novell.com/ifolder/server/3.5/20060330-000/src/%{name}-%{version}.tar.gz
# Source0-md5:	ab69bc5fe3c27bbdd0f32b4ed056f130
URL:		http://www.ifolder.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	compat-libstdc++-3.1
BuildRequires:	e2fsprogs-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libflaim-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	log4net-devel
BuildRequires:	mono
BuildRequires:	mono-compat-links
BuildRequires:	mono-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
#Requires:	log4net
#Requires:	mono-core >= 1.1.8
#Requires:	mono-data >= 1.1.8
#Requires:	mono-web >= 1.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/ifolder3
%define		_libexecdir		/usr/lib/ifolder3
%define		_simiasdatadir	/var/lib/ifolder3

%description
iFolder is a simple and secure storage solution that can increase your
productivity by enabling you to back up, access and manage your
personal files from anywhere, at anytime. Once you have installed
iFolder, you simply save your files locally as you have always
done and iFolder automatically updates the files on a network server
and delivers them to the other machines you use.

Sponsored by Novell, the iFolder project is built on the mono/.Net
framework to integrate seamlessly into existing desktop environments

%prep
%setup -q

# remove svn control files
find -name .svn -print0 | xargs -0 rm -rf

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--libexecdir=%{libexecdir} \
	--sysconfdir=%{sysconfdir} \
	--with-simiasdatadir=%{simiasdatadir}
#  --with-ndoc-path=PATH        path to dir that contains NDocConsole.exe [NONE]
#  --with-client-setup     configure simias to run as a client. [Default=FALSE]
#  --with-pic              try to use only PIC/non-PIC objects [default=use both]

%{__make}

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

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
