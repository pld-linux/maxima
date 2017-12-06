#
# Conditional build:
%bcond_without	emacs	# Emacs mode

Summary:	Maxima Symbolic Computation Program
Summary(pl.UTF-8):	Program do obliczeń symbolicznych Maxima
Name:		maxima
Version:	5.41.0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/maxima/%{name}-%{version}.tar.gz
# Source0-md5:	972c51384d7895c88d78eb045c6aedb2
Source2:	%{name}-mode-init.el
Patch0:		%{name}-info.patch
Patch1:		%{name}-missed-files.patch
Patch3:		x%{name}-doc.patch
Patch4:		%{name}-install.patch
Patch5:		%{name}-info-compressed.patch
URL:		http://maxima.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	clisp
%{?with_emacs:BuildRequires:	emacs}
BuildRequires:	gettext-tools
BuildRequires:	perl-base >= 5
BuildRequires:	python >= 2
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	texinfo
%requires_eq	clisp
Requires:	gzip
Suggests:	gnuplot
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

%package -n bash-completion-maxima
Summary:	Bash completion for Maxima
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla Maximy
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-maxima
Bash completion for Maxima.

%description -n bash-completion-maxima -l pl.UTF-8
Bashowe dopełnianie parametrów dla Maximy.

%package xmaxima
Summary:	Tcl/Tk GUI interface for Maxima
Summary(pl.UTF-8):	Graficzny interfejs Tcl/Tk dla Maximy
Group:		Applications/Math
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	shared-mime-info
Requires:	tk

%description xmaxima
Tcl/Tk GUI interface for maxima.

%description xmaxima -l pl.UTF-8
Graficzny interfejs Tcl/Tk dla Maximy.

%package -n bash-completion-xmaxima
Summary:	Bash completion for XMaxima
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla XMaximy
Group:		Applications/Shells
Requires:	%{name}-xmaxima = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-xmaxima
Bash completion for XMaxima.

%description -n bash-completion-xmaxima -l pl.UTF-8
Bashowe dopełnianie parametrów dla XMaximy.

%package src
Summary:	Maxima lisp source code
Summary(pl.UTF-8):	Pliki źródłowe Maximy
Group:		Development

%description src
Maxima lisp source code.

%description src -l pl.UTF-8
Pliki źródłowe Maximy.

%package doc
Summary:	Maxima documentation
Summary(pl.UTF-8):	Dokumentacja dla Maximy
Group:		Documentation

%description doc
Maxima documentation.

%description doc -l pl.UTF-8
Dokumentacja dla Maximy.

%package -n emacs-maxima-pkg
Summary:	Emacs mode for Maxima
Summary(pl.UTF-8):	Tryb Maximy dla Emacsa
Group:		Applications/Math
Requires:	emacs-common

%description -n emacs-maxima-pkg
Emacs mode files for Maxima.

%description -n emacs-maxima-pkg -l pl.UTF-8
Tryb Maximy dla Emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
touch doc/info/{maximahtml.mk,category-macros.texi} src/{clisp,cmucl,gcl}-depends.mk

%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-clisp \
	--enable-gettext

# TODO: --enable-lang-de[-utf8?] --enable-lang-es[-utf8?] --enable-lang-pt[-utf8?] --enable-lang-pt_BR[-utf8?]
# for localized info pages

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*

install -Dp doc/man/ru/maxima.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1/maxima.1

%if %{with emacs}
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}/site-start.d
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{version}/emacs $RPM_BUILD_ROOT%{_emacs_lispdir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_emacs_lispdir}/site-start.d
%else
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/%{version}/emacs
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	xmaxima
%update_mime_database
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun	xmaxima
%update_mime_database
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%triggerin doc -- %{name} = %{epoch}:%{version}
if [ -d %{_docdir}/%{name}-doc-%{version} ]; then
	ln -snf %{_docdir}/%{name}-doc-%{version} %{_datadir}/%{name}/%{version}/doc
fi

%triggerun doc -- %{name} = %{epoch}:%{version}
rm %{_datadir}/%{name}/%{version}/doc || :

%triggerpostun doc -- %{name} = %{epoch}:%{version}
if [ -d %{_docdir}/%{name}-doc-%{version} -a \
	-d %{_datadir}/%{name}/%{version} ]; then
	ln -snf %{_docdir}/%{name}-doc-%{version} %{_datadir}/%{name}/%{version}/doc
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog-5* README
%attr(755,root,root) %{_bindir}/maxima
%attr(755,root,root) %{_bindir}/rmaxima
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%attr(755,root,root) %{_libdir}/%{name}/%{version}/mgnuplot
%dir %{_libdir}/%{name}/%{version}/binary-clisp
%attr(755,root,root) %{_libdir}/%{name}/%{version}/binary-clisp/lisp.run
%{_libdir}/%{name}/%{version}/binary-clisp/maxima.mem
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/demo
%{_datadir}/%{name}/%{version}/share
%{_datadir}/%{name}/%{version}/tests
%{_mandir}/man1/maxima.1*
%lang(ru) %{_mandir}/ru/man1/maxima.1*
%{_infodir}/imaxima.info*
%{_infodir}/maxima.info*
%{_infodir}/maxima-index.lisp
# packages
%{_infodir}/abs_integrate.info*
%{_infodir}/drawutils.info*
%{_infodir}/kovacicODE.info*
%{_infodir}/logic.info*

%files -n bash-completion-maxima
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/maxima
%{_datadir}/bash-completion/completions/rmaxima

%files xmaxima
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmaxima
%{_datadir}/%{name}/%{version}/xmaxima
%{_desktopdir}/xmaxima.desktop
%{_infodir}/xmaxima.info*
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/mime/packages/x-maxima-out.xml
%{_pixmapsdir}/maxima-new.png
%{_pixmapsdir}/maxima-new.svg
%{_pixmapsdir}/text-x-maxima-out.svg
%{_pixmapsdir}/text-x-maximasession.svg

%files -n bash-completion-xmaxima
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/xmaxima

%if %{with emacs}
%files -n emacs-maxima-pkg
%defattr(644,root,root,755)
%{_emacs_lispdir}/%{name}
%{_emacs_lispdir}/site-start.d/%{name}-mode-init.el
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}

%files src
%defattr(644,root,root,755)
%{_usrsrc}/maxima-%{version}
