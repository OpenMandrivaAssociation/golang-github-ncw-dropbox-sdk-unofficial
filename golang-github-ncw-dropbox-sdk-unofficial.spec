# Run tests in check section
%bcond_without check

%global goipath         github.com/ncw/dropbox-sdk-go-unofficial
%global commit          5d9f46f9862ae5f65e264e178de6ce2c41a32d40

%global common_description %{expand:
An unofficial Go SDK for integrating with the Dropbox API v2.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: An unofficial Go SDK for integrating with the Dropbox API v2
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/oauth2)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-ncw-dropbox-sdk-go-unofficial-devel = %{version}-%{release}
Obsoletes: golang-github-ncw-dropbox-sdk-go-unofficial-devel < 0-0.3.20180314git5d9f46f
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git5d9f46f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180328git5d9f46f
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170530git5d9f46f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170530git5d9f46f
- First package for Fedora

