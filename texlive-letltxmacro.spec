Name:		texlive-letltxmacro
Version:	53022
Release:	2
Summary:	Let assignment for LaTeX macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/letltxmacro
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letltxmacro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letltxmacro.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letltxmacro.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX's \let assignment does not work for LaTeX macros with
optional arguments or for macros that are defined as robust
macros by \DeclareRobustCommand. This package defines
\LetLtxMacro that also takes care of the involved internal
macros.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/letltxmacro
%{_texmfdistdir}/tex/latex/letltxmacro
%doc %{_texmfdistdir}/doc/latex/letltxmacro

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
