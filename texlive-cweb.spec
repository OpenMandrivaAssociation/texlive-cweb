%global tl_name cweb
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	CWEB for ANSI-C/C++ compilers
Group:		Publishing
URL:		https://www.ctan.org/pkg/cwebbin
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(cweb.bin)
Requires:	texlive(iftex)
Requires:	texlive(kpathsea)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A highly portable and extended version of Levy/Knuth CWEB 3.64c for
UNIX, Windows, Mac (and possibly other operating systems). TeX macros,
CWEB macros, and NLS catalogs are included for German, French
(partially), and Italian program documentation on any machine. Major
features: Thoroughly updated code base; several bug fixes; clean
compilation (with both C and TeX) on at least four different
architectures. Added CTWILL program with tools and utilities for brave
users; including introductory manpage. Internationalization of CTANGLE,
CWEAVE, and CTWILL with "GNU gettext utilities". New code base for CWEB
in TeX Live 2019, incorporating all features of the TL 2018 version and
adding new features from CWEBbin. As of November 2019 CTAN no longer
holds a copy of this material. Please go to the package's github
repository for more information.

