#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	SOAP
%define		pnam	Transport-TCP
Summary:	SOAP::Transport::TCP - TCP Transport Support for SOAP::Lite
Name:		perl-SOAP-Transport-TCP
Version:	0.715
Release:	2
License:	artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SOAP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1f50f3c4ca3efd1062ed64468d9363d
URL:		http://search.cpan.org/dist/SOAP-Transport-TCP/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(SOAP::Lite) >= 0.712
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TCP Transport Support for SOAP::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SOAP/Transport/*.pm
#{perl_vendorlib}/SOAP/Transport/TCP
%{_mandir}/man3/*
