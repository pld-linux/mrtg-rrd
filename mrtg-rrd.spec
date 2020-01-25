# TODO:
# - finish it
# - take a look at debian stuff - they have a lot of fixes
Summary:	Multi Router Traffic Grapher
Summary(pl.UTF-8):	MRTG - generator obrazów obciążenia łącz
Name:		mrtg-rrd
Version:	0.7
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://ftp.linux.cz/pub/linux/people/jan_kasprzak/mrtg-rrd/%{name}-%{version}.tar.gz
# Source0-md5:	132c5910582531a72855da3144cf18c0
URL:		http://www.fi.muni.cz/~kas/mrtg-rrd/
BuildRequires:	rrdtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgidir		/usr/share/%{name}

%description
Multi Router Traffic Grapher.

%description -l pl.UTF-8
MRTG - generator obrazów obciążenia łącz.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cgidir}

install mrtg-rrd.cgi $RPM_BUILD_ROOT%{_cgidir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ TODO
%dir %{_cgidir}
%attr(755,root,root) %{_cgidir}/*.cgi
