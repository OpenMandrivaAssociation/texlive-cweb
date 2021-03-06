Name:		texlive-cweb
Version:	3.64b
Release:	2
Summary:	A Web system in C
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/c_cpp/cweb
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cweb.bin

%description
The Cweb system is a system for Structured Software
Documentation (also known as Literate Programming) in the
programming language C.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/cweb
%doc %{_mandir}/man1/ctangle.1*
%doc %{_texmfdistdir}/doc/man/man1/ctangle.man1.pdf
%doc %{_mandir}/man1/cweave.1*
%doc %{_texmfdistdir}/doc/man/man1/cweave.man1.pdf
%doc %{_mandir}/man1/cweb.1*
%doc %{_texmfdistdir}/doc/man/man1/cweb.man1.pdf
%doc %{_texmfdistdir}/doc/plain/cweb

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
