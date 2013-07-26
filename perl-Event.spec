%define upstream_name	 Event
%define upstream_version 1.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.21
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Event/Event-1.21.tar.gz

BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Fast, generic event loop

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc ANNOUNCE INSTALL README TODO Tutorial.pdf ChangeLog
%{perl_vendorarch}/Event*
%{perl_vendorarch}/auto/Event
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.180.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.180.0-1
+ Revision: 687340
- update to new version 1.18

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1
+ Revision: 677327
- update to new version 1.17

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.150.0-1
+ Revision: 672615
- update to new version 1.15

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-2mdv2011.0
+ Revision: 555255
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2010.1
+ Revision: 461740
- update to 1.13

* Thu Aug 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2010.0
+ Revision: 421624
- update to 1.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 403160
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.11-2mdv2009.0
+ Revision: 268471
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.0
+ Revision: 209325
- update to new version 1.11

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.1
+ Revision: 156177
- update to new version 1.10
- update to new version 1.10

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.09-2mdv2008.1
+ Revision: 152070
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2008.0
+ Revision: 46524
- update to new version 1.09


* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2007.0
+ Revision: 84656
- new version
- Import perl-Event

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-3mdv2007.0
- Rebuild

* Sat May 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-2mdk
- better source URL
- test in %%check

* Thu May 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.06-1mdk
- 1.06
- Add ChangeLog in docs

* Fri Apr 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdk 
- new release
- spec cleanup
- better url
- no more explicit perl requires
- rpmbuilupdate aware

* Thu Mar 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.04-1mdk
- 1.04

* Fri Feb 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03
- make tests

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 1.00-2mdk
- rebuild for new perl

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-1mdk
- 1.00
- use %%makeinstall_std macro

* Tue Apr 27 2004 Stefan van der Eijk <stefan@mandrake.org> 0.88-1mdk
- 0.88


