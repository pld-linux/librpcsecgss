Summary:	rpcsec_gss implementation library
Summary(pl):	Biblioteka implementuj±ca rpcsec_gss
Name:		librpcsecgss
Version:	0.5
Release:	2
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/librpcsecgss/%{name}-%{version}.tar.gz
# Source0-md5:	0c8c7df876e6fe8994b231d2aa2012b2
Patch0:		%{name}-configure.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	heimdal-devel >= 0.7
BuildRequires:	libtool
# it's checked before heimdal (which is preferred in PLD)
BuildConflicts:	krb5-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librpcsecgss allows secure RPC communication using the rpcsec_gss
protocol.

%description -l pl
librpcsecgss umo¿liwia bezpieczn± komunikacjê RPC przy u¿yciu
protoko³u rpcsec_gss.

%package devel
Summary:	Development files for librpcsecgss library
Summary(pl):	Pliki programistyczne biblioteki librpcsecgss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	heimdal-devel

%description devel
Development files for librpcsecgss library.

%description devel -l pl
Pliki programistyczne biblioteki librpcsecgss.

%package static
Summary:	Static librpcsecgss library
Summary(pl):	Statyczna biblioteka librpcsecgss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librpcsecgss library.

%description static -l pl
Statyczna biblioteka librpcsecgss.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-krb5=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/librpcsecgss.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpcsecgss.so
%{_libdir}/librpcsecgss.la

%files static
%defattr(644,root,root,755)
%{_libdir}/librpcsecgss.a
