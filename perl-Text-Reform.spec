%define module	Text-Reform
%define version	1.11
%define release %mkrel 5

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	Manual text wrapping and reformatting
License:	Artistic
Group:		Text tools
URL:		http://search.cpan.org/author/DCONWAY/Text-Reform-1.11/lib/Text/Reform.pm
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Requires:       perl
BuildArch:	noarch

%description
The form() subroutine may be exported from the module. It takes a series
of format (or "picture") strings followed by replacement values, inter-
polates those values into each picture string, and returns the result.
The effect is similar to the inbuilt perl format mechanism, although the
field specification syntax is simpler and some of the formatting beha-
viour is more sophisticated.

%prep
%setup -q -n %{module}-%{version}
%__perl -pi -e "s,/usr/local/bin/perl,%__perl," *.pl
# muhahahah

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT

eval `perl '-V:installarchlib'`
install -d $RPM_BUILD_ROOT/$installarchlib

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/Text/*
%{_mandir}/*/*

