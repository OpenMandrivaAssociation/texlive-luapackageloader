%global tl_name luapackageloader
%global tl_revision 54779

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Allow LuaTeX to load external Lua packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luapackageloader
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luapackageloader.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luapackageloader.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(iftex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows LuaTeX to load packages from the default
package.path and package.cpath locations. This could be useful to load
external Lua modules, including modules installed via LuaRocks. This
package requires ifluatex.

