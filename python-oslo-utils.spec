# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.utils

Name:           python-oslo-utils
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Utility library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-oslo-config
Requires:       python-oslo-i18n
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-six >= 1.9.0
Requires:       python-netaddr >= 0.7.12
Requires:       python-netifaces >= 0.10.4
Requires:       python-debtcollector >= 0.3.0
Requires:       pytz

%description
The OpenStack Oslo Utility library.
* Documentation: http://docs.openstack.org/developer/oslo.utils
* Source: http://git.openstack.org/cgit/openstack/oslo.utils
* Bugs: http://bugs.launchpad.net/oslo


%package doc
Summary:    Documentation for the Oslo Utility library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
# for API autodoc
BuildRequires:  python-netifaces
BuildRequires:  python-debtcollector

%description doc
Documentation for the Oslo Utility library.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/oslo_utils
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth

%files doc
%doc html
%license LICENSE

%changelog
