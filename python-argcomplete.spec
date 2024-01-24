# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-argcomplete
Epoch: 100
Version: 3.5.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Bash tab completion for argparse
License: Apache-2.0
URL: https://github.com/kislyuk/argcomplete/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_prefix}/share/bash-completion/completions
install -Dpm644 ./argcomplete/bash_completion.d/_python-argcomplete %{buildroot}%{_prefix}/share/bash-completion/completions/python-argcomplete
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-argcomplete
Summary: Bash tab completion for argparse
Requires: python3
Provides: python3-argcomplete = %{epoch}:%{version}-%{release}
Provides: python3dist(argcomplete) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-argcomplete = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(argcomplete) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-argcomplete = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(argcomplete) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-argcomplete
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

%files -n python%{python3_version_nodots}-argcomplete
%license LICENSE.rst
%{_bindir}/*
%{python3_sitelib}/*
%{_prefix}/share/bash-completion/completions/python-argcomplete
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-argcomplete
Summary: Bash tab completion for argparse
Requires: python3
Provides: python3-argcomplete = %{epoch}:%{version}-%{release}
Provides: python3dist(argcomplete) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-argcomplete = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(argcomplete) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-argcomplete = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(argcomplete) = %{epoch}:%{version}-%{release}

%description -n python3-argcomplete
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

%files -n python3-argcomplete
%license LICENSE.rst
%{_bindir}/*
%{python3_sitelib}/*
%{_prefix}/share/bash-completion/completions/python-argcomplete
%endif

%changelog
