#
# Conditional build:
%bcond_with	libgssapi	# use libgssapi glue instead of heimdal directly
#
Summary:	rpcsec_gss implementation library
Summary(pl):	Biblioteka implementuj±ca rpcsec_gss
Name:		librpcsecgss
Version:	0.13
Release:	1
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/librpcsecgss/%{name}-%{version}.tar.gz
# Source0-md5:	024143270490e0e252832c9f64499645
Patch0:		%{name}-heimdal.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
%if %{with libgssapi}
BuildRequires:	libgssapi-devel >= 0.9
BuildRequires:	pkgconfig
Requires:	libgssapi >= 0.9
%else
BuildRequires:	heimdal-devel
%endif
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
%if %{with libgssapi}
Requires:	libgssapi-devel >= 0.9
%else
Requires:	heimdal-devel
%endif

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
%if %{without libgssapi}
%patch0 -p1
sed -i -e 's,gssapi/gssapi\.h,gssapi.h,' include/rpcsecgss/rpc/auth_gss.h \
	src/{authgss_prot,auth_gss,svc_auth_gss}.c
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	librpcsecgss_la_LIBADD='$(GSSAPI_LIBS)'

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
%{_includedir}/rpcsecgss
%{_pkgconfigdir}/librpcsecgss.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librpcsecgss.a
