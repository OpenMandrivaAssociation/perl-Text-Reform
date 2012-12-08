%define upstream_name	 Text-Reform
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Manual text wrapping and reformatting
License:	Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{perl_vendorlib}/Text/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-4mdv2012.0
+ Revision: 765761
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-3
+ Revision: 764287
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-2
+ Revision: 667397
- mass rebuild

* Mon Sep 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 432323
- update to 1.20

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.12.2-2mdv2010.0
+ Revision: 426596
- rebuild

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.2-1mdv2009.1
+ Revision: 270511
- new version
- spec cleanup

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.11-7mdv2009.0
+ Revision: 224383
- rebuild

* Tue Jan 22 2008 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.11-6mdv2008.1
+ Revision: 156503
- force 5.10.0 rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-5mdv2008.0
+ Revision: 23304
- rebuild


* Fri Mar 31 2006 Buchan Milne <bgmilne@mandriva.org> 1.11-4mdk
- Rebuild
- use mkrel

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.11-3mdk
- rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.11-2mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Thu May 15 2003 Han Boetes <han@linux-mandrake.com> 1.11-1mdk
- first build for mandrake.

