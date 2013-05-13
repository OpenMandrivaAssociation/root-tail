%define name root-tail
%define version 1.2
%define release  12

Summary:   Root-tail prints text directly to an X11 root window
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    http://www.goof.com/pcg/marc/data/%{name}-%{version}.tar.bz2
URL:	   http://www.goof.com/pcg/marc/root-tail.html 
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
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
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,755)
%doc README Changes
%attr(755,root,root) 
%{_bindir}/*
%{_mandir}/man1/*
%_datadir/applications/mandriva-*
#%{_iconsdir}/%{name}.png
#%{_liconsdir}/%{name}.png
#%{_miconsdir}/%{name}.png


%changelog
* Sun Mar 18 2012 GÃ¶tz Waschk <waschk@mandriva.org> 1.2-11mdv2012.0
+ Revision: 785474
- yearly rebuild

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2-10
+ Revision: 645876
- relink against libmysqlclient.so.18

* Thu Feb 10 2011 Funda Wang <fwang@mandriva.org> 1.2-9
+ Revision: 637092
- tighten BR

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.2-8mdv2011.0
+ Revision: 260278
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.2-7mdv2009.0
+ Revision: 251350
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2-5mdv2008.1
+ Revision: 148352
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2-5mdv2008.0
+ Revision: 51176
- Import root-tail


  
* Mon Jul 10 2006 Götz Waschk <waschk@mandriva.org> 1.2-5mdv2007.0
- fix buildrequires

* Wed Jul  5 2006 Götz Waschk <waschk@mandriva.org> 1.2-4mdv2007.0
- fix prefix
- new menu
- fix buildrequires

* Wed Dec 14 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.2-3mdk
- Rebuild
- use mkrel

* Mon Dec 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2-2mdk
- fix buildrequires

* Tue Aug 31 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2-1mdk
- fix rpmlint warning about the menu description
- fix man page
- add source URL
- New release 1.2

* Mon Apr 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1-1mdk
- new version

* Wed Feb 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9-1mdk
- drop prefix
- new version

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-3mdk
- rebuild

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 0.2-2mdk
- rebuild

* Wed Nov  6 2002 Götz Waschk <waschk@linux-mandrake.com> 0.2-1mdk
- initial Mandrake package based on the work from Marcel Pol <mpol@gmx.net> 
- spec cleanup

* Sat Oct 12 2002 Marcel Pol <mpol@gmx.net> 
- 0.2

* Sat Jul 14 2001 Marcel Pol <mpol@gmx.net> 0.0.10-1mdk
- Update to 0.10
- Added menu entry

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.4B-2mdk
- BM

* Mon Jun 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.4B-1mdk
- new in contribs
- used srpm provided by Max Heijndijk <cchq@wanadoo.nl>
