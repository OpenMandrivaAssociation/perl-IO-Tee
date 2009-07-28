%define upstream_name	 IO-Tee
%define upstream_version 0.64

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Multiplex output to multiple output handles 
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TL/TLOWERY/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/IO
