%define upstream_name	 IO-Tee
%define upstream_version 0.66
Name:		perl-%{upstream_name}
Version:	0.66
Release:	1

Summary:	Multiplex output to multiple output handles 
License:	GPL
Group:		Development/Perl
URL:		https://github.com/neilb/IO-Tee
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/IO-Tee-0.66.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


