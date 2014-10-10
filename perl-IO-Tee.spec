%define upstream_name	 IO-Tee
%define upstream_version 0.64

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Multiplex output to multiple output handles 
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TL/TLOWERY/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
IO::Tee objects can be used to multiplex input and output in two different
ways. The first way is to multiplex output to zero or more output handles. The
IO::Tee constructor, given a list of output handles, returns a tied handle that
can be written to. When written to (using print or printf), the IO::Tee object
multiplexes the output to the list of handles originally passed to the
constructor. As a shortcut, you can also directly pass a string or an array
reference to the constructor, in which case IO::File::new is called for you
with the specified argument or arguments.

The second way is to multiplex input from one input handle to zero or more
output handles as it is being read. The IO::Tee constructor, given an input
handle followed by a list of output handles, returns a tied handle that can be
read from as well as written to. When written to, the IO::Tee object
multiplexes the output to all handles passed to the constructor, as described
in the previous paragraph. When read from, the IO::Tee object reads from the
input handle given as the first argument to the IO::Tee constructor, then
writes any data read to the output handles given as the remaining arguments to
the constructor.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/IO


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2010.0
+ Revision: 402559
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.64-5mdv2009.0
+ Revision: 257358
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.64-3mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-3mdv2008.0
+ Revision: 86511
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-2mdv2007.0
- Rebuild

* Thu Oct 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdk
- first mdk release

