#
# Conditional build:
%bcond_with	tests	# do perform "make test" (test/schemas files are missing)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python object model built on JSON schema and JSON patch
Name:		python-warlock
Version:	1.3.3
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/w/warlock/warlock-%{version}.tar.gz
# Source0-md5:	746aba989d97762948e5fca6601f283f
URL:		https://pypi.python.org/pypi/warlock
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-jsonpatch >= 0.10
BuildRequires:	python-jsonschema >= 0.7
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-jsonpatch >= 0.10
BuildRequires:	python3-jsonschema >= 0.7
BuildRequires:	python3-six
%endif
%endif
Requires:	python-jsonpatch >= 0.10
Requires:	python-jsonschema >= 0.7
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Build self-validating python objects using JSON schemas.

%package -n python3-warlock
Summary:	Python object model built on JSON schema and JSON patch
Group:		Libraries/Python
Requires:	python3-jsonpatch >= 0.10
Requires:	python3-jsonschema >= 0.7
Requires:	python3-six

%description -n python3-warlock
Build self-validating python objects using JSON schemas.

%prep
%setup -q -n warlock-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=build-2/lib %{__python} -m unittest discover -t test test_core
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=build-2/lib %{__python} -m unittest discover -t test test_core
%endif
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
%doc README.md
%{py_sitescriptdir}/warlock
%{py_sitescriptdir}/warlock-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-warlock
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/warlock
%{py3_sitescriptdir}/warlock-%{version}-py*.egg-info
%endif

