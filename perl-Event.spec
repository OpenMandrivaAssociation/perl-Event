%define upstream_name	 Event
%define upstream_version 1.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz
Source100: %{name}.rpmlintrc

BuildRequires:	perl-devel

%description
Fast, generic event loop

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%clean 

%install
%makeinstall_std

%files
%doc ANNOUNCE INSTALL README TODO Tutorial.pdf ChangeLog
%{perl_vendorarch}/Event*
%{perl_vendorarch}/auto/Event
%{_mandir}/*/*
