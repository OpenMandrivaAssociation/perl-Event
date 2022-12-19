%define debug_package %{nil}

Summary:	Event module for perl
Name:		perl-Event
Version:	1.28
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/Event
Source0:	https://www.cpan.org/modules/by-module/Event/Event-%{version}.tar.gz
Source100: %{name}.rpmlintrc

BuildRequires:	perl-devel

%files
%doc ANNOUNCE INSTALL README TODO Tutorial.pdf
%{perl_vendorarch}/Event*
%{perl_vendorarch}/auto/Event
%{_mandir}/*/*

#----------------------------------------------------------------------------

%description
Fast, generic event loop

%prep
%autosetup -p1 -n Event-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

