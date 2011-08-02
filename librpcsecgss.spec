#
# Conditional build:
%bcond_with	gssglue	# use GSSGLUE layer instead of linking with Heimdal Kerberos directly
#
Summary:	rpcsec_gss implementation library
Summary(pl.UTF-8):	Biblioteka implementująca rpcsec_gss
Name:		librpcsecgss
Version:	0.19
Release:	3
License:	BSD/MIT
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/librpcsecgss/%{name}-%{version}.tar.gz
# Source0-md5:	b45ed565bdc3099023aa35830ec92997
Patch0:		%{name}-heimdal.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%if %{with gssglue}
BuildRequires:	libgssglue-devel >= 0.1
%else
BuildRequires:	heimdal-devel
%endif
BuildRequires:	libtool
BuildRequires:	pkgconfig
%if %{with gssglue}
Requires:	libgssglue >= 0.1
%else
Requires:	heimdal-libs
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librpcsecgss allows secure RPC communication using the rpcsec_gss
protocol.

%description -l pl.UTF-8
librpcsecgss umożliwia bezpieczną komunikację RPC przy użyciu
protokołu rpcsec_gss.

%package devel
Summary:	Development files for librpcsecgss library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki librpcsecgss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with gssglue}
Requires:	libgssglue-devel >= 0.1
%else
Requires:	heimdal-devel
%endif

%description devel
Development files for librpcsecgss library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki librpcsecgss.

%package static
Summary:	Static librpcsecgss library
Summary(pl.UTF-8):	Statyczna biblioteka librpcsecgss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librpcsecgss library.

%description static -l pl.UTF-8
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
	--with-gssapiimpl=%{?with_gssglue:libgssglue}%{!?with_gssglue:heimdal-gssapi}
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
%attr(755,root,root) %ghost %{_libdir}/librpcsecgss.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpcsecgss.so
%{_libdir}/librpcsecgss.la
%{_includedir}/rpcsecgss
%{_pkgconfigdir}/librpcsecgss.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librpcsecgss.a
