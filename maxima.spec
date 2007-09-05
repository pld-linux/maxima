#
# TODO:
#	- separate subpackages with: xmaxima, doc, src, (emacs?)
Summary:	Maxima Symbolic Computation Program
Summary(pl.UTF-8):	Program do obliczeń symbolicznych Maxima
Name:		maxima
Version:	5.13.0
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/maxima/%{name}-%{version}.tar.gz
# Source0-md5:	7317ba22fc485554b15aceb6bc22542b
Source1:	x%{name}.desktop
Source2:	x%{name}.sh
Patch0:		%{name}-info.patch
URL:		http://maxima.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clisp
BuildRequires:	texinfo
%requires_eq	clisp
Requires:	gnuplot
Requires:	tk
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

%description -l pl.UTF-8
Maxima jest pakietem do pełnych obliczeń matematycznych. Ma duże
możliwości symbolicznych obliczeń na wielomianach, macierzach,
funkcjach wymiernych, całkowania, stosowania metody Todda-Coxetera,
rysowania, obliczeń na wielkich liczbach. Posiada symboliczny debugger
kodu źródłowego w maximie. Maxima bazuje na oryginalnej Macsyma
utworzonej w MIT w roku 1970. Ma dobrą obsługę błędów, nie ma wycieków
pamięci. Przychodzi z setkami testów. Od połowy lat 80-tych za rozwój
projektu odpowiada William Schelter z University of Texas. Więcej
informacji na stronie http://www.ma.utexas.edu/maxima.html. Ostatnio
udało mu się uzyskać pozwolenie DOE na opublikowanie Maximy na
licencji GPL.

%prep
%setup -q
%patch0 -p1
touch doc/info/{maximahtml.mk,category-macros.texi} src/{clisp,cmucl,gcl}-depends.mk

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-clisp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
cp -f $RPM_BUILD_ROOT%{_datadir}/%{name}/%{version}/xmaxima/%{name}-icon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man?/*
%{_infodir}/maxima.info*
