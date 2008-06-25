%define module	Text-Reform
%define version	1.12.2
%define release %mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	Manual text wrapping and reformatting
License:	Artistic
Group:		Text tools
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Term/%{module}-v%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The form() subroutine may be exported from the module. It takes a series
of format (or "picture") strings followed by replacement values, inter-
polates those values into each picture string, and returns the result.
The effect is similar to the inbuilt perl format mechanism, although the
field specification syntax is simpler and some of the formatting beha-
viour is more sophisticated.

%prep
%setup -q -n %{module}-v%{version}
%__perl -pi -e "s,/usr/local/bin/perl,%__perl," *.pl
# muhahahah

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/Text/*
%{_mandir}/*/*

