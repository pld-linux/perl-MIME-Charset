#
############################################################
#
# NOTE
# - use the SOURCES/pldcpan.pl script for new perl packages
#   also available in pldcpan package.
#
############################################################
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Charset
Summary:	-
Summary(pl.UTF-8):	-
Name:		perl-MIME-Charset
Version:	1.006
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a764906fe10ca4b61badbc2a00cc58fc
URL:		http://search.cpan.org/dist/MIME-Charset/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# most of CPAN modules have generic URL (substitute pdir and pnam here)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	CC="%{__cc}"
#	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MIME/Charset.pm
%dir %{perl_vendorlib}/MIME/Charset
%{perl_vendorlib}/MIME/Charset/Defaults.pm.sample
%{perl_vendorlib}/MIME/Charset/JA_JP.pod
%{perl_vendorlib}/MIME/Charset/_Compat.pm
%{_mandir}/man3/*
