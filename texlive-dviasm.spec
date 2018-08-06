# revision 26313
# category Package
# catalog-ctan /dviware/dviasm
# catalog-date 2012-04-10 15:00:16 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-dviasm
Version:	20180303
Release:	1
Summary:	A utility for editing DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dviasm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviasm.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/dviasm/dviasm.py dviasm
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120410-1
+ Revision: 812230
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100116-2
+ Revision: 751177
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100116-1
+ Revision: 718276
- texlive-dviasm
- texlive-dviasm
- texlive-dviasm
- texlive-dviasm

