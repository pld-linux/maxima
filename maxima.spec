#
# TODO:
#	- separate subpackages with: xmaxima, doc, src, (emacs?)
Summary:	Maxima Symbolic Computation Program
Summary(pl):	Program do obliczeñ symbolicznych Maxima
Name:		maxima
Version:	5.9.1
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/maxima/%{name}-%{version}.zip
# Source0-md5:	7e993cd7867a4ae26e558d1fd2d87bfa
Source1:	x%{name}.desktop
Patch0:		%{name}-info.patch
URL:		http://maxima.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clisp
BuildRequires:	texinfo
# for .zip source
BuildRequires:	unzip
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

%description -l pl
Maxima jest pakietem do pe³nych obliczeñ matematycznych. Ma du¿e
mo¿liwo¶ci symbolicznych obliczeñ na wielomianach, macierzach,
funkcjach wymiernych, ca³kowania, stosowania metody Todda-Coxetera,
rysowania, obliczeñ na wielkich liczbach. Posiada symboliczny debugger
kodu ¼ród³owego w maximie. Maxima bazuje na oryginalnej Macsyma
utworzonej w MIT w roku 1970. Ma dobr± obs³ugê b³êdów, nie ma wycieków
pamiêci. Przychodzi z setkami testów. Od po³owy lat 80-tych za rozwój
projektu odpowiada William Schelter z University of Texas. Wiêcej
informacji na stronie http://www.ma.utexas.edu/maxima.html. Ostatnio
uda³o mu siê uzyskaæ pozwolenie DOE na opublikowanie Maximy na
licencji GPL.

%prep
%setup -q
%patch0 -p1
touch doc/info/maximahtml.mk src/{clisp,cmucl,gcl}-depends.mk

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-clisp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/*
%{_mandir}/man?/*
%{_infodir}/maxima.info*
