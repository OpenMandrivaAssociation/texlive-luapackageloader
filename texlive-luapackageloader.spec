Name:		texlive-luapackageloader
Version:	54779
Release:	1
Summary:	Allow LuaTeX to load external Lua packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luapackageloader
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapackageloader.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapackageloader.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows LuaTeX to load packages from the default
package.path and package.cpath locations. This could be useful
to load external Lua modules, including modules installed via
LuaRocks. This package requires ifluatex.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/luapackageloader
%doc %{_texmfdistdir}/doc/luatex/luapackageloader

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
