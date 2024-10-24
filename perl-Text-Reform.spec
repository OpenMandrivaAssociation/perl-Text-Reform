%define modname	Text-Reform

Summary:	Manual text wrapping and reformatting
Name:		perl-%{modname}
Version:	1.20
Release:	1
License:	Artistic
Group:		Text tools
Url:		https://metacpan.org/pod/Text::Reform
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
The form() subroutine may be exported from the module. It takes a series
of format (or "picture") strings followed by replacement values, inter-
polates those values into each picture string, and returns the result.
The effect is similar to the inbuilt perl format mechanism, although the
field specification syntax is simpler and some of the formatting beha-
viour is more sophisticated.

%prep
%setup -qn %{modname}-%{version}
%__perl -pi -e "s,/usr/local/bin/perl,%__perl," *.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README MANIFEST Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*
