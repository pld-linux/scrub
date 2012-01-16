Summary:	Destroy data on disk using DoD 5520.22-M or NNSA NAP-14.x algorithms
Summary(pl.UTF-8):	Niszczenie danych na dysku przy użyciu algorytmu DoD 5520.22-M lub NNSA NAP-14.x
Name:		scrub
Version:	2.4.1
Release:	1
License:	GPL v2+
Group:		Applications/File
Source0:	http://diskscrub.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	852d0051837e58a902097d3ff5356a3a
URL:		http://code.google.com/p/diskscrub/
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility writes patterns on files or disk devices to make
retrieving the data more difficult. It operates in one of three modes:
1) the special file corresponding to an entire disk is scrubbed and
all data on it is destroyed. 2) a regular file is scrubbed and only
the data in the file (and optionally its name in the directory entry)
is destroyed. 3) a regular file is created, expanded until the file
system is full, then scrubbed as in 2).

Scrub implements user-selectable pattern algorithms that are compliant
with DoD 5520.22-M or NNSA NAP-14.x.

%description -l pl.UTF-8
To narzędzie pisze po plikach lub urządzeniach dyskowych wzorce, aby
utrudnić odzyskanie danych. Działa w jednym z trzech trybów: 1) czyści
plik specjalny odpowiadający całemu dyskowi, niszcząc w ten sposób
wszystkie dane na nim; 2) czyści zwykły plik, niszcząc tylko dane z
tego pliku (i opcjonalnie jego nazwę w katalogu); 3) tworzy zwykły
plik, powiększa go do wypełnienia systemu plików, a następnie go
czyści w sposób 2).

scrub implementuje algorytmy z wzorcem obieralnym przez użytkownika,
zgodne z DoD 5520.22-M lub NNSA NAP-14.x.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog DISCLAIMER NEWS
%attr(755,root,root) %{_bindir}/scrub
%{_mandir}/man1/scrub.1*
