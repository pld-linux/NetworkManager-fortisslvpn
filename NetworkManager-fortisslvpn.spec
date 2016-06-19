Summary:	NetworkManager VPN integration for Fortinet SSLVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z Fortinet SSLVPN
Name:		NetworkManager-fortisslvpn
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-fortisslvpn/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	dbf98c77aa69e791505f0c2525270f7f
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
%requires_eq	ppp
Requires:	openfortivpn
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for Fortinet SSLVPN.

%description -l pl.UTF-8
Integracja NetworkManagera z Fortinet SSLVPN.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la \
	$RPM_BUILD_ROOT%{_libdir}/pppd/plugins/*.la

%find_lang NetworkManager-fortisslvpn

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-fortisslvpn.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-fortisslvpn-properties.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%attr(755,root,root) %{_libdir}/nm-fortisslvpn-auth-dialog
%attr(755,root,root) %{_libdir}/nm-fortisslvpn-service
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-fortisslvpn-pppd-plugin.so
%{_libdir}/NetworkManager/VPN/nm-fortisslvpn-service.name
%{_sysconfdir}/NetworkManager/VPN/nm-fortisslvpn-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml
%dir %{_datadir}/gnome-vpn-properties/fortisslvpn
%{_datadir}/gnome-vpn-properties/fortisslvpn/nm-fortisslvpn-dialog.ui
