Summary:	Check shell scripts for common bash-specific contructs
Name:		checkbashisms
Version:	2.10.64
Release:	1
Source0:	%{name}.pl
Source1:	%{name}.1
License:	GPL v2+
Group:		Development
URL:		http://packages.debian.org/sid/devscripts
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
checkbashisms checks whether a /bin/sh script contains any common
bash-specific contructs.

It is extracted from the Debian devscripts package.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
