Name:           glite-info-create-core
Version:        0.1.0
Release:        1%{?dist}
Summary:        Core components for the glite-info-create framework.
Group:          Development/Tools
License:        Apache Software License 2
URL:            http://svnweb.cern.ch/guest/gridinfo/glite-info-static-core
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Source:         %{name}-%{version}.src.tgz
%description
Core components for the glite-info-create framework.

%prep
%setup -q -c

%build 

%install
rm -rf %{buildroot}
make prefix=%{buildroot} install 


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/sbin/glite-info-create

%doc
/usr/share/doc/%{name}-%{version}/README.txt

%changelog
* Mon Feb 15 2010 Laurence Field <laurence.field@cern.ch> - 0.1.0-1
- First release
