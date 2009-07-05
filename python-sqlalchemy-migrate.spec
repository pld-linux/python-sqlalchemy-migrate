%define 	module migrate
Summary:	Schema migration tools for SQLAlchemy
Summary(pl.UTF-8):	Narzędzia do migracji struktury bazy dla SQLAlchemy
Name:		python-sqlalchemy-%{module}
Version:	0.5.4
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
# http://sqlalchemy-migrate.googlecode.com/files/sqlalchemy-migrate-0.5.4.tar.gz
Source0:	http://sqlalchemy-migrate.googlecode.com/files/sqlalchemy-%{module}-%{version}.tar.gz
# Source0-md5:	7ad9e6d6dd6df701fc596bcb87380271
URL:		http://code.google.com/p/sqlalchemy-migrate/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-SQLAlchemy >= 0.5.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

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
