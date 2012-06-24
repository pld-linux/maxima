Summary:	Maxima Symbolic Computation Program
Summary(pl):	Program do oblicze� symbolicznych Maxima
Name:		maxima
Version:	5.9.0rc1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://prdownloads.sourceforge.net/maxima/%{name}-%{version}.tar.gz
URL:		http://maxima.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clisp
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
Maxima jest pakietem do pe�nych oblicze� matematycznych. Ma du�e
mo�liwo�ci symbolicznych oblicze� na wielomianach, macierzach,
funkcjach wymiernych, ca�kowania, stosowania metody Todda-Coxetera,
rysowania, oblicze� na wielkich liczbach. Posiada symboliczny debugger
kodu �r�d�owego w maximie. Maxima bazuje na oryginalnej Macsyma
utworzonej w MIT w roku 1970. Ma dobr� obs�ug� b��d�w, nie ma wyciek�w
pami�ci. Przychodzi z setkami test�w. Od po�owy lat 80-tych za rozw�j
projektu odpowiada William Schelter z University of Texas. Wi�cej
informacji na stronie http://www.ma.utexas.edu/maxima.html. Ostatnio
uda�o mu si� uzyska� pozwolenie DOE na opublikowanie Maximy na
licencji GPL.

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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_infodir}/*
