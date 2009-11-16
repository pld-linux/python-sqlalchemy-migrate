%define 	module migrate
Summary:	Schema migration tools for SQLAlchemy
Summary(pl.UTF-8):	Narzędzia do migracji struktury bazy dla SQLAlchemy
Name:		python-sqlalchemy-%{module}
Version:	0.5.4
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	http://sqlalchemy-migrate.googlecode.com/files/sqlalchemy-%{module}-%{version}.tar.gz
# Source0-md5:	7ad9e6d6dd6df701fc596bcb87380271
URL:		http://code.google.com/p/sqlalchemy-migrate/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-SQLAlchemy >= 0.5.1
Requires:	python-decorator >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schema migration tools for SQLAlchemy, designed to support an agile approach to database design, and make it easier to keep development and production databases in sync, as schema changes are required.

%description -l pl.UTF-8
Narzędzia migracji struktury bazy danych dla SQLAlchemy, zaprojektowane aby wspierać sprawne projektowanie i ułatwiać utrzymanie wersji rozwojowych i produkcyjnych baz danych w synchornizacji w miare zmian ich struktury.

%prep
%setup -q -n sqlalchemy-%{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/migrate
%attr(755,root,root) %{_bindir}/migrate-repository

## %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
##%{py_sitedir}/*.py[co]
## %attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/%{module}
##%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/sqlalchemy_migrate-*.egg-info
##%endif
