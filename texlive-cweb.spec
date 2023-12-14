Name:		texlive-cweb
Version:	68702
Release:	1
Summary:	A Web system in C
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/c_cpp/cweb
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.doc.r%{version}.tar.xz
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
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
