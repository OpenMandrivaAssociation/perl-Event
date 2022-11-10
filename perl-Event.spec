%define debug_package %{nil}

%define upstream_name	 Event
%define upstream_version 1.28

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	https://www.cpan.org/modules/by-module/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz
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
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

