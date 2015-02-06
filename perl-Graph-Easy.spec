%define upstream_name    Graph-Easy
%define upstream_version 0.75
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse Graphviz text into Graph::Easy


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Graph/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
'Graph::Easy' lets you generate graphs consisting of various shaped nodes
connected by edges (with optional labels).

It can read and write graphs in a varity of formats, as well as render them
via its own grid-based layouter.

Since the layouter works on a grid (manhattan layout), the output is most
usefull for flow charts, network diagrams, or hierarchy trees.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm t/pod.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE CHANGES
%{_bindir}/graph-easy
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*



