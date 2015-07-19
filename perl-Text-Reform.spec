%define modname	Text-Reform
%define modver	1.20

Summary:	Manual text wrapping and reformatting
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The form() subroutine may be exported from the module. It takes a series
of format (or "picture") strings followed by replacement values, inter-
polates those values into each picture string, and returns the result.
The effect is similar to the inbuilt perl format mechanism, although the
field specification syntax is simpler and some of the formatting beha-
viour is more sophisticated.

%prep
%setup -qn %{modname}-%{modver}
%__perl -pi -e "s,/usr/local/bin/perl,%__perl," *.pl
# muhahahah

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*

