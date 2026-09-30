Summary:        This module provides support to authenticate against PostgreSQL tables for PAM-enabled appliations
Name:           pam_pgsql
Version:        0.7.3.2
Release:        1%{?dist}
Epoch:          1
License:        GPLv2+
Group:          System Environment/Base
Source:         https://github.com/pam-pgsql/pam-pgsql/archive/release-%{version}.tar.gz
Patch0:         pam_pgsql-crypt-include.patch
URL:            https://github.com/pam-pgsql/pam-pgsql
BuildRequires:  autoconf automake libtool libgcrypt-devel pam-devel
%if 0%{?rhel} >= 10
# postgresql-private-devel conflicts with libpq-devel and its pg_config needs server-devel
BuildRequires:  postgresql-server-devel
%else
BuildRequires:  libpq-devel
%endif
Requires:       pam

%global debug_package %{nil}

%description
This module provides support to authenticate against PostgreSQL
tables for PAM-enabled appliations.

This module is based in part on the FreeBSD pam_unix module, and
the Debian pam_mysql module, but was written from scratch using
the two as a reference.

%prep
%setup -q -n pam-pgsql-release-%{version}
%patch -P 0 -p1
./autogen.sh
autoreconf -fiv

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/doc/pam-pgsql/CHANGELOG
/usr/share/doc/pam-pgsql/COPYRIGHT
/usr/share/doc/pam-pgsql/CREDITS
/usr/share/doc/pam-pgsql/README
/usr/share/doc/pam-pgsql/sample.sql
/usr/lib64/security/pam_pgsql.so

%changelog
* Mon May 27 2019 Jamie Curnow <jc@j21.com> - 0.7.3.2-1
- Initial spec
