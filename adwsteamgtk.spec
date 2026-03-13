Name:           adwsteamgtk
Version:        0.8.0
# Using autorelease ensures COPR can increment the release number automatically
Release:        %autorelease
Summary:        A GTK frontend for the Adwaita Steam theme

License:        GPL-3.0-or-later
URL:            https://github.com/Foldex/AdwSteamGtk
# COPR's SCM mode will automatically replace this with the generated git tarball
Source0:        %{url}/archive/main/AdwSteamGtk-main.tar.gz

BuildArch:      noarch

# Core build requirements based on the meson.build file
BuildRequires:  meson >= 0.59.0
BuildRequires:  ninja-build
BuildRequires:  blueprint-compiler
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  python3-devel

# Runtime requirements
Requires:       python3
Requires:       gtk4
Requires:       libadwaita

%description
An installer and updater for the Adwaita Steam theme.

%prep
%autosetup -n AdwSteamGtk-main

%build
# The project uses meson with default options
%meson
%meson_build

%install
%meson_install
# The meson file explicitly imports i18n and includes a 'po' directory
%find_lang AdwSteamGtk

%files -f AdwSteamGtk.lang
%{_bindir}/adwaita-steam-gtk
%{_datadir}/adwaita-steam-gtk/
%{_datadir}/applications/io.github.Foldex.AdwSteamGtk.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.Foldex.AdwSteamGtk*.svg
%{_datadir}/glib-2.0/schemas/io.github.Foldex.AdwSteamGtk.gschema.xml
%{_datadir}/metainfo/io.github.Foldex.AdwSteamGtk.appdata.xml

%changelog
%autochangelog
