#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Charset
Summary:	Charset Informations for MIME
Summary(pl.UTF-8):	Informacje o zestawach znaków dla MIME
Name:		perl-MIME-Charset
Version:	1.012.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71440416376248c31aa3bef753fae28d
URL:		http://search.cpan.org/dist/MIME-Charset/
BuildRequires:	perl-Encode >= 1:1.98
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Charset provides informations about character sets used for MIME
messages on Internet.

%description -l pl.UTF-8
Moduł Perla zawierający informacje o zestawach znaków używanych przez
MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--skipdeps

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/ja/man3

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/POD2/JA/MIME/Charset.pod
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::MIME::Charset.3pm $RPM_BUILD_ROOT%{_mandir}/ja/man3/MIME::Charset.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MIME/Charset.pm
%dir %{perl_vendorlib}/MIME/Charset
%{perl_vendorlib}/MIME/Charset/Defaults.pm.sample
%{perl_vendorlib}/MIME/Charset/_Compat.pm
%{perl_vendorlib}/MIME/Charset/UTF.pm
%{_mandir}/man3/MIME::Charset.3pm*
%lang(ja) %{_mandir}/ja/man3/MIME::Charset.3pm*
