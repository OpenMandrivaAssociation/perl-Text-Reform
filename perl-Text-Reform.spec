%define upstream_name	 Text-Reform
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Manual text wrapping and reformatting
License:	Artistic
Group:		Text tools
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The form() subroutine may be exported from the module. It takes a series
of format (or "picture") strings followed by replacement values, inter-
polates those values into each picture string, and returns the result.
The effect is similar to the inbuilt perl format mechanism, although the
field specification syntax is simpler and some of the formatting beha-
viour is more sophisticated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
