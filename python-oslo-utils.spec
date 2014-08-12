%global pypi_name oslo.utils

Name:           python-oslo-utils
Version:        XXX
Release:        1%{?dist}
Summary:        Oslo Utils

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr


%description
oslo.utils library

%prep
%setup -q -n oslo.utils-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}

#%check
#%{__python} setup.py test

%files
%doc README.rst LICENSE
%dir %{python_sitelib}/oslo
%{python_sitelib}/oslo/utils
%{python_sitelib}/oslo.utils-%{version}*

%changelog
* Tue Aug 12 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package.
