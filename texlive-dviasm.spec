%global tl_name dviasm
%global tl_revision 71902

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A utility for editing DVI files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dviasm
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviasm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviasm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dviasm.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Python script to support changing or creating DVI files via
disassembling into text, editing, and then reassembling into binary
format. It supports advanced features such as adding a preprint number
or watermarks.

