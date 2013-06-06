%define upstream_name    Graph-Easy
%define upstream_version 0.72
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.72
Release:	1

Summary:	Parse Graphviz text into Graph::Easy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Graph/Graph-Easy-0.72.tar.gz

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

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.700.0-2mdv2011.0
+ Revision: 656926
- rebuild for updated spec-helper

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.700.0-1mdv2011.0
+ Revision: 596527
- update to new version 0.70

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.690.0-1mdv2011.0
+ Revision: 552314
- update to 0.69

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2010.0
+ Revision: 444015
- import perl-Graph-Easy


* Thu Sep 17 2009 cpan2dist 0.64-1mdv
- initial mdv release, generated with cpan2dist

