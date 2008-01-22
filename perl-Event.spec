%define module	Event
%define name	perl-%{module}
%define version	1.10
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/Event/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Fast, generic event loop

%prep
%setup -q -n %{module}-%{version}

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


