Summary:	rpcsec_gss implementation library
Summary(pl.UTF-8):	Biblioteka implementująca rpcsec_gss
Name:		librpcsecgss
Version:	0.15
Release:	1
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/librpcsecgss/%{name}-%{version}.tar.gz
# Source0-md5:	7d39d6aab44d99aacd197be6d592bbf3
Patch0:		%{name}-pc.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libgssglue-devel >= 0.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libgssglue >= 0.1
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
Requires:	libgssglue-devel >= 0.1

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
%configure
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
%{_includedir}/rpcsecgss
%{_pkgconfigdir}/librpcsecgss.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librpcsecgss.a
