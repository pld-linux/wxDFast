#
# TODO:
# - descriptions
# - do something bout the wx-config stuff (patch?)
# - ensure proper BR & Rs (I've never developped any wx stuff)
#
%define		realname	wxdfast
Summary:	Download manager/accelerator
Summary(pl.UTF-8):	Zarządca/przyspieszacz pobierania
Name:		wxDFast
Version:	0.6.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/dfast/%{realname}_%{version}.tar.gz
# Source0-md5:	05c2a71cc8f811d1ad5916fce29b7b3a
URL:		http://dfast.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	wxWidgets-devel >= 2.6.0
BuildRequires:	wxWidgets-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Download manager/accelerator.

%description -l pl.UTF-8
Zarządca/przyspieszacz pobierania.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%lang(pt_BR) %doc ChangeLog.br README.br
%attr(755,root,root) %{_bindir}/*
%{_datadir}/wxdfast
%{_desktopdir}/wxdfast.desktop
%{_pixmapsdir}/wxdfast.png
%{_mandir}/man1/wxdfast.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/wxdfast.1*
