%define module pyright
#disable tests, requires unpackaged nodejs_wheel module
%bcond tests 0

Name:		python-pyright
Version:	1.1.410
Release:	1
Summary:	Command line wrapper for pyright
License:	MIT
Group:		Development/Python
URL:		https://github.com/RobertCraigie/pyright-python
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(nodeenv)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-subprocess)
# BuildRequires:	python%%{pyver}dist(nodejs-wheel)
%endif

%description
Command line wrapper for pyright

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# ignore tests that require internet access
pytest \
	--ignore tests/test_main.py \
	--ignore tests/test_langserver.py \
	--ignore tests/test_node.py
%endif

%files
%doc README.md
%{_bindir}/%{module}{,-python,-langserver,-python-langserver}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
