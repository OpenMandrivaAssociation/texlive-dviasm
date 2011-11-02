Name:		texlive-dviasm
Version:	20100116
Release:	1
Summary:	A utility for editing DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dviasm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviasm.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-dviasm.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

%description
A Python script to support changing or creating DVI files via
disassembling into text, editing, and then reassembling into
binary format. It supports advanced features such as adding a
preprint number or watermarks.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/dviasm
%{_texmfdistdir}/scripts/dviasm/dviasm.py

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/dviasm/dviasm.py dviasm
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
