%define name root-tail
%define version 1.2
%define release %mkrel 5

Summary:   Root-tail prints text directly to an X11 root window
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    http://www.goof.com/pcg/marc/data/%{name}-%{version}.tar.bz2
URL:	   http://www.goof.com/pcg/marc/root-tail.html 
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: X11-devel
BuildRequires: rman
BuildRequires: imake
BuildRequires: gccmakedep
License:   GPL
Group:     Monitoring

%description
Displays a given file anywhere on your X11 root window
with a transparent background.
It was made because I am very lazy and this was easier than
making a new rxvt pixmap each time I changed my background
to simulate that transparent effect.

%prep
%setup -q

%build
xmkmf -a
make CDEBUGFLAGS="${RPM_OPT_FLAGS}" \
     CXXDEBUGFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf %buildroot
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
cp root-tail ${RPM_BUILD_ROOT}%{_bindir}
cp root-tail.man ${RPM_BUILD_ROOT}%{_mandir}/man1/root-tail.1

# Menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%_bindir/%{name} -g 80x25+100+50 -font fixed /var/log/messages,black" \
needs="X11" \
section="System/Monitoring" \
title="Root-tail" longtitle="Root-tail prints text directly to a root window" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Root-Tail
Comment=Root-tail prints text directly to a root window
Exec=%_bindir/%{name} -g 80x25+100+50 -font fixed /var/log/messages,black
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF


#icon
#install -d $RPM_BUILD_ROOT/%{_iconsdir}
#install -d $RPM_BUILD_ROOT/%{_liconsdir}
#install -d $RPM_BUILD_ROOT/%{_miconsdir}
#bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
#bzcat %{SOURCE2} > $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
#bzcat %{SOURCE3} > $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
 
%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,755)
%doc README Changes
%attr(755,root,root) 
%{_bindir}/*
%{_mandir}/man1/*
%{_menudir}/*
%_datadir/applications/mandriva-*
#%{_iconsdir}/%{name}.png
#%{_liconsdir}/%{name}.png
#%{_miconsdir}/%{name}.png
