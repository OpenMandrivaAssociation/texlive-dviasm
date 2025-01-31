Name:		texlive-dviasm
Version:	71902
Release:	1
Summary:	A utility for editing DVI files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dviasm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviasm.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-dviasm.bin = %{EVRD}

%description
A Python script to support changing or creating DVI files via
disassembling into text, editing, and then reassembling into
binary format. It supports advanced features such as adding a
preprint number or watermarks.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/dviasm
%{_texmfdistdir}/scripts/dviasm/dviasm.py

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/dviasm/dviasm.py dviasm
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
