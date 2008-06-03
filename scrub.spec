Summary:	Destroy data on disk using DoD 5520.22-M or NNSA NAP-14.x algorithms
Summary(pl.UTF-8):	Niszczenie danych na dysku przy użyciu algorytmu DoD 5520.22-M lub NNSA NAP-14.x
Name:		scrub
Version:	1.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/diskscrub/%{name}-%{version}.tar.bz2
# Source0-md5:	597a9c55aa031f2650546becf24cb2b0
URL:		https://computing.llnl.gov/linux/scrub.html
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
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -s scrub $RPM_BUILD_ROOT%{_bindir}
install scrub.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS DISCLAIMER COPYING
%attr(755,root,root) %{_bindir}/scrub
%{_mandir}/man*/*
