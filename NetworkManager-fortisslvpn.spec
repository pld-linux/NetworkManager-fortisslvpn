# TODO:
# - nm-fortisslvpn user (for dropping pppd privileges)
#
# Conditional build:
%bcond_without	gtk4	# Gtk4 version of editor plugin (GNOME 42+)

Summary:	NetworkManager VPN integration for Fortinet SSLVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z Fortinet SSLVPN
Name:		NetworkManager-fortisslvpn
Version:	1.4.0
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-fortisslvpn/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	33e1a0c50b9032621748ff166f57fa1d
Patch0:		%{name}-ppp2.5.patch
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.19
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
BuildRequires:	libnma-devel >= 1.8.33
%{?with_gtk4:BuildRequires:	libnma-gtk4-devel >= 1.8.33}
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.5.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
Requires:	libnma >= 1.8.33
Requires:	libsecret >= 0.18
%requires_eq_to	ppp ppp-plugin-devel
Requires:	openfortivpn
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for Fortinet SSLVPN.

%description -l pl.UTF-8
Integracja NetworkManagera z Fortinet SSLVPN.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{?with_gtk4:--with-gtk4} \
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
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%if %{with gtk4}
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-fortisslvpn-editor.so
%endif
%attr(755,root,root) %{_libexecdir}/nm-fortisslvpn-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-fortisslvpn-pinentry
%attr(755,root,root) %{_libexecdir}/nm-fortisslvpn-service
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-fortisslvpn-pppd-plugin.so
%{_prefix}/lib/NetworkManager/VPN/nm-fortisslvpn-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml
