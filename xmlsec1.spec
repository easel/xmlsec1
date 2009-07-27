Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.2.11
Release: 4
License: MIT
Group: Development/Libraries
Source: ftp://ftp.aleksey.com/pub/xmlsec/releases/xmlsec1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.aleksey.com/xmlsec/
Requires: libxml2 >= 2.6.0
Requires: libxslt >= 1.1.0
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.1.0
Prefix: %{_prefix}
Docdir: %{_docdir}

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package devel
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support.
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: libxml2-devel >= 2.6.0
Requires: libxslt-devel >= 1.1.0
Requires: openssl-devel >= 0.9.6
Requires: zlib-devel
Requires: pkgconfig

%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package openssl
Summary: OpenSSL crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.6.0
Requires: libxslt >= 1.1.0
Requires: openssl >= 0.9.6
BuildRequires: openssl-devel >= 0.9.6

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library

%post openssl
/sbin/ldconfig

%postun openssl
/sbin/ldconfig

%package openssl-devel
Summary: OpenSSL crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-openssl = %{version}
Requires: libxml2-devel >= 2.6.0
Requires: libxslt-devel >= 1.1.0
Requires: openssl >= 0.9.6
Requires: openssl-devel >= 0.9.6

%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL

%package gnutls
Summary: GNUTls crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.6.0
Requires: libxslt >= 1.1.0
Requires: libgcrypt >= 1.2.0
Requires: gnutls >= 1.0.20
BuildRequires: libgcrypt-devel >= 1.2.0
BuildRequires: gnutls-devel >= 1.0.20

%description gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library

%post gnutls
/sbin/ldconfig

%postun gnutls
/sbin/ldconfig

%package gnutls-devel
Summary: GNUTls crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-openssl = %{version}
Requires: libxml2-devel >= 2.6.0
Requires: libxslt-devel >= 1.1.0
Requires: libgcrypt >= 1.2.0
Requires: gnutls >= 1.0.20
Requires: libgcrypt-devel >= 1.2.0
Requires: gnutls-devel >= 1.0.20

%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls

%package nss
Summary: NSS crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.4.24
Requires: libxslt >= 1.0.20
Requires: nss >= 3.2
Requires: nspr
BuildRequires: nss-devel >= 3.2
BuildRequires: nspr-devel

%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package nss-devel
Summary: NSS crypto plugin for XML Security Library
Group: Development/Libraries
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-nss = %{version}
Requires: libxml2-devel >= 2.4.24
Requires: libxslt-devel >= 1.0.20
Requires: nss-devel >= 3.2
Requires: nspr-devel

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS

%prep
%setup -q

%build
%configure
#
# Note: it seems that this may break on older version of Red Hat,
#       and that replacing the following line with just "make" can
#       fix the problem
#
make

# positively ugly but only sane way to get around #192756
sed 's+/lib64+/$archlib+g' < xmlsec1-config | sed 's+/lib+/$archlib+g' | sed 's+ -DXMLSEC_NO_SIZE_T++' > xmlsec1-config.$$ && mv xmlsec1-config.$$ xmlsec1-config

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/include/xmlsec1
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

%makeinstall
#make prefix=$RPM_BUILD_ROOT%{prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1.1*

%{prefix}/lib*/libxmlsec1.so.*
%{prefix}/bin/xmlsec1

%files devel
%defattr(-, root, root)

%{prefix}/bin/xmlsec1-config
%dir %{prefix}/include/xmlsec1
%dir %{prefix}/include/xmlsec1/xmlsec
%dir %{prefix}/include/xmlsec1/xmlsec/private
%{prefix}/include/xmlsec1/xmlsec/*.h
%{prefix}/include/xmlsec1/xmlsec/private/*.h
%{prefix}/lib*/libxmlsec1.so
%{prefix}/lib*/libxmlsec1.*a
%{prefix}/lib*/pkgconfig/xmlsec1.pc
%{prefix}/lib*/xmlsec1Conf.sh
%dir %{prefix}/share/doc/xmlsec1
%{prefix}/share/doc/xmlsec1/*
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1-config.1*
%{_datadir}/aclocal/xmlsec1.m4

%files openssl
%defattr(-, root, root)

%{prefix}/lib*/libxmlsec1-openssl.so.*

%files openssl-devel
%defattr(-, root, root)

%dir %{prefix}/include/xmlsec1/xmlsec/openssl
%{prefix}/include/xmlsec1/xmlsec/openssl/*.h
%{prefix}/lib*/libxmlsec1-openssl.*a
%{prefix}/lib*/libxmlsec1-openssl.so
%{prefix}/lib*/pkgconfig/xmlsec1-openssl.pc

%files gnutls
%defattr(-, root, root)

%{prefix}/lib*/libxmlsec1-gnutls.so.*

%files gnutls-devel
%defattr(-, root, root)

%dir %{prefix}/include/xmlsec1/xmlsec/gnutls
%{prefix}/include/xmlsec1/xmlsec/gnutls/*.h
%{prefix}/lib*/libxmlsec1-gnutls.*a
%{prefix}/lib*/libxmlsec1-gnutls.so
%{prefix}/lib*/pkgconfig/xmlsec1-gnutls.pc

%files nss
%defattr(-, root, root)

%{prefix}/lib*/libxmlsec1-nss.so.*

%files nss-devel
%defattr(-, root, root)

%dir %{prefix}/include/xmlsec1/xmlsec/nss
%{prefix}/include/xmlsec1/xmlsec/nss/*.h
%{prefix}/lib*/libxmlsec1-nss.*a
%{prefix}/lib*/libxmlsec1-nss.so
%{prefix}/lib*/pkgconfig/xmlsec1-nss.pc

%changelog
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.11-2
- rebuild with new openssl

* Fri Jul 11 2008 Daniel Veillard <veillard@redhat.com> - 1.2.11-1
- update to new upstream release 1.2.11
- rebuild for gnutls update

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.9-10.1
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2.9-9
 - Rebuild for deps

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-8.1
- rebuild

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com> - 1.2.9-8
- rebuilt with new gnutls

* Thu Jun  8 2006 Daniel Veillard <veillard@redhat.com> - 1.2.9-7
- oops libxmlsec1.la was still there, should fix #171410 and #154142

* Thu Jun  8 2006 Daniel Veillard <veillard@redhat.com> - 1.2.9-6
- Ugly patch and sed based changes to work around #192756 xmlsec1-config
  multilib problem

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1.2.9-5
- move .so symlinks to -devel subpackage

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 15 2005 Christopher Aillon <caillon@redhat.com> 1.2.9-4
- NSS has been split out of the mozilla package, so require that now
  and update separate_nspr.patch to account for the new NSS as well

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Tomas Mraz <tmraz@redhat.com> 1.2.9-3
- rebuilt due to gnutls library revision
* Wed Nov  9 2005 <veillard@redhat.com> 1.2.9-2
- rebuilt due to openssl library revision
* Tue Sep 20 2005 <veillard@redhat.com> 1.2.9-1
- update from upstream, release done in July
- apparently nss is now available on ppc64
* Mon Aug  8 2005 <veillard@redhat.com> 1.2.8-3
- rebuilt with new gnutls
- nspr has been split to a separate package
* Fri Jul  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.8-2
- Enabling the mozilla-nss crypto backend
* Fri Jul  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.8-1
- update from upstream, needed for openoffice
* Tue Mar  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.7-4
- rebuilt with gcc4
* Wed Feb 23 2005 Daniel Veillard <veillard@redhat.com> 1.2.7-1
- Upstream release of 1.2.7, mostly bug fixes plus new functions
  to GetKeys from simple store and X509 handling.
* Wed Feb  9 2005 Daniel Veillard <veillard@redhat.com> 1.2.6-4
- Adding support for GNUTls crypto backend
* Wed Sep  1 2004 Daniel Veillard <veillard@redhat.com> 1.2.6-3
- adding missing ldconfig calls
* Thu Aug 26 2004 Daniel Veillard <veillard@redhat.com> 1.2.6-2
- updated with upstream release from Aleksey
* Mon Jun 21 2004 Daniel Veillard <veillard@redhat.com> 1.2.5-2
- rebuilt
* Mon Apr 19 2004 Daniel Veillard <veillard@redhat.com> 1.2.5-1
- updated with upstream release from Aleksey
* Wed Feb 11 2004 Daniel Veillard <veillard@redhat.com> 1.2.4-1
- updated with upstream release from Aleksey
* Tue Jan  6 2004 Daniel Veillard <veillard@redhat.com> 1.2.3-1
- updated with upstream release from Aleksey
* Wed Nov 12 2003 Daniel Veillard <veillard@redhat.com> 1.2.2-1
- updated with upstream release from Aleksey, specific patches should
  have been integrated now.
* Thu Nov  6 2003 Daniel Veillard <veillard@redhat.com> 1.2.1-1
- initial packaging based on the upstream one and libxml2 one.
- desactivated mozilla-nss due to detection/architecture problems
