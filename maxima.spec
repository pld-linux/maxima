Summary:	Maxima Symbolic Computation Program
Summary(pl):	Program do obliczeñ symbolicznych Maxima
Name:		maxima
Version:	5.9.0rc1
Release:	1
License:	GPL
Group:		Applications/Math
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clisp
Url:		http://maxima.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/maxima/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maxima is a full symbolic computation program. It is full featured
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats. It has a
symbolic debugger source level debugger for maxima code. Maxima is
based on the original Macsyma developed at MIT in the 1970's. It is
quite reliable, and has good garbage collection, and no memory leaks.
It comes with hundreds of self tests. William Schelter at University
of Texas, has been responsible for development since the mid 1980's.
See http://www.ma.utexas.edu/maxima.html for more information. He has
recently been able to get DOE to allow him to distribute Maxima under
the GPL.

%description -l pl
Maxima jest pakietem do pe³nych obliczeñ matematycznych. Ma du¿e
mo¿liwo¶ci symbolicznych obliczeñ na polynomials, matrycach, funkcjach
rational, integracji, Todd-coxeter, grafach, wielkich liczbach.
Posiada symbolicznych debugger kodu ¼ród³owego w maximie. Maxima
bazuje na oryginalnej Macsyma utworzonej w MIT w roku 1970. Posiada
dobr± obs³ugê b³êdów, brakuje dziur w pamiêci. Przychodzi z setkami
testów. William Schelter na University of Texas by³ odpowiedzialny za
tworzenie od roku 1980. Zobacz na stronê
http://www.ma.utexas.edu/maxima.html dla dalszych informacji. Ostatnio
wypu¶ci³ Maxima na licencji GPL co pozwoli³o na swobodn± jej
redystrybucjê.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
touch doc/info/maximahtml.mk src/{clisp,cmucl,gcl}-depends.mk

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_mandir}/man?/*
%{_datadir}/%{name}
