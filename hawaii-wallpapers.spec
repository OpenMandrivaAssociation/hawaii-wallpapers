%define debug_package %{nil}

Summary:	Hawaii wallpapers
Name:		hawaii-wallpapers
Version:	0.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
Source0:	https://github.com/hawaii-desktop/%{name}/archive/%{name}-%{version}.tar.xz
Source1:	hawaii-wallpapers.rpmlintrc
BuildRequires:	cmake
BuildRequires:	cmake(ECM)

%track
prog %{name} = {
	url = https://github.com/hawaii-desktop/%{name}/archive/
	regex = "v(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Wallpapers for the Hawaii desktop environment.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%dir %{_datadir}/backgrounds/hawaii
%{_datadir}/backgrounds/hawaii/*.*g

