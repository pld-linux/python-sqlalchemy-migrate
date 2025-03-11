#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Schema migration tools for SQLAlchemy
Summary(pl.UTF-8):	Narzędzia do migracji struktury bazy dla SQLAlchemy
Name:		python-sqlalchemy-migrate
Version:	0.13.0
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sqlalchemy-migrate/sqlalchemy-migrate-%{version}.tar.gz
# Source0-md5:	86572c92ae84334907f5e3a2cecc92a6
URL:		https://pypi.org/project/sqlalchemy-migrate/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 1.8
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Tempita >= 0.4
BuildRequires:	python-decorator
BuildRequires:	python-ibm_db_sa
BuildRequires:	python-scripttest
BuildRequires:	python-six >= 1.7.0
BuildRequires:	python-sqlalchemy >= 0.9.6
BuildRequires:	python-sqlparse
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-pbr >= 1.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Tempita >= 0.4
BuildRequires:	python3-decorator
BuildRequires:	python3-ibm_db_sa
BuildRequires:	python3-scripttest
BuildRequires:	python3-six >= 1.7.0
BuildRequires:	python3-sqlalchemy >= 0.9.6
BuildRequires:	python3-sqlparse
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2 >= 1.6.7
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schema migration tools for SQLAlchemy, designed to support an agile
approach to database design, and make it easier to keep development
and production databases in sync, as schema changes are required.

%description -l pl.UTF-8
Narzędzia migracji struktury bazy danych dla SQLAlchemy,
zaprojektowane aby wspierać zwinne podejście do projektowania baz i
ułatwiać utrzymanie wersji rozwojowych i produkcyjnych baz danych w
synchronizacji w miarę zmian ich struktury.

%package -n python3-sqlalchemy-migrate
Summary:	Schema migration tools for SQLAlchemy
Summary(pl.UTF-8):	Narzędzia do migracji struktury bazy dla SQLAlchemy
Group:		Development/Languages/Python

%description -n python3-sqlalchemy-migrate
Schema migration tools for SQLAlchemy, designed to support an agile
approach to database design, and make it easier to keep development
and production databases in sync, as schema changes are required.

%description -n python3-sqlalchemy-migrate -l pl.UTF-8
Narzędzia migracji struktury bazy danych dla SQLAlchemy,
zaprojektowane aby wspierać zwinne podejście do projektowania baz i
ułatwiać utrzymanie wersji rozwojowych i produkcyjnych baz danych w
synchronizacji w miarę zmian ich struktury.

%package apidocs
Summary:	API documentation for Python SQLAlchemy Migrate module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona SQLAlchemy Migrate
Group:		Documentation

%description apidocs
API documentation for Python SQLAlchemy Migrate module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona SQLAlchemy Migrate.

%prep
%setup -q -n sqlalchemy-migrate-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc/source html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.rst TODO
%attr(755,root,root) %{_bindir}/migrate
%attr(755,root,root) %{_bindir}/migrate-repository
%{py_sitescriptdir}/migrate
%{py_sitescriptdir}/sqlalchemy_migrate-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sqlalchemy-migrate
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.rst TODO
%{py3_sitescriptdir}/migrate
%{py3_sitescriptdir}/sqlalchemy_migrate-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/source/_build/html/{_static,*.html,*.js}
%endif
