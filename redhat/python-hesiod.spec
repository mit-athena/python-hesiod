Name:		python-hesiod
Version:	0.2.12
Release:	1%{?dist}
Summary:	Python bindings for Hesiod

Group:		Development/Languages
License:	MIT
URL:		https://github.com/mit-athena/python-hesiod/
Source0:	https://debathena.mit.edu/redist/%{name}-%{version}.tar.gz

BuildRequires:	Pyrex
BuildRequires:	hesiod-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel

%description
PyHesiod provides a set of Python bindings for Hesiod, the Project
Athena service name resolution protocol used at MIT and elsewhere.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="-I%{_includedir}/et" %{__python2} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{python_sitearch}/*


%changelog
* Wed Aug  6 2014 Alex Chernyakhovsky <achernya@mit.edu> - 0.2.12-1
- Initial packaging.
