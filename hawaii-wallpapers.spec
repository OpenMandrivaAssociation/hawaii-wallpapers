%define debug_package %{nil}

Summary:	Hawaii wallpapers
Name:		hawaii-wallpapers
Version:	0.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-wallpapers.rpmlintrc
BuildRequires:	cmake

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/
	regex = "%{name}-(__VER__)\.tar\.gz"
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
%{_datadir}/backgrounds/hawaii
