Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.2.8
Release: 2
License: MIT
Group: Development/Libraries
Source: ftp://ftp.aleksey.com/pub/xmlsec/releases/xmlsec1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
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

# mozilla-nss is nor available on ppc64
%ifnarch ppc64
%package nss
Summary: NSS crypto plugin for XML Security Library
Group: Development/Libraries 
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.4.24
Requires: libxslt >= 1.0.20
Requires: mozilla-nss >= 1.4
BuildRequires: mozilla-nss-devel >= 1.4

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
Requires: mozilla-nss-devel >= 1.4

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS
%endif

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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/include/xmlsec1
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

%makeinstall
#make prefix=$RPM_BUILD_ROOT%{prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

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
%{prefix}/lib*/libxmlsec1.so
%{prefix}/bin/xmlsec1

%files devel
%defattr(-, root, root)  

%{prefix}/bin/xmlsec1-config
%{prefix}/include/xmlsec1/xmlsec/*.h
%{prefix}/include/xmlsec1/xmlsec/private/*.h
%{prefix}/lib*/libxmlsec1.*a
%{prefix}/lib*/pkgconfig/xmlsec1.pc
%{prefix}/lib*/xmlsec1Conf.sh
%{prefix}/share/doc/xmlsec1/* 
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1-config.1*

%files openssl
%defattr(-, root, root)  

%{prefix}/lib*/libxmlsec1-openssl.so.*
%{prefix}/lib*/libxmlsec1-openssl.so

%files openssl-devel
%defattr(-, root, root)  

%{prefix}/include/xmlsec1/xmlsec/openssl/*.h
%{prefix}/lib*/libxmlsec1-openssl.*a
%{prefix}/lib*/pkgconfig/xmlsec1-openssl.pc

%files gnutls
%defattr(-, root, root)  

%{prefix}/lib*/libxmlsec1-gnutls.so.*
%{prefix}/lib*/libxmlsec1-gnutls.so

%files gnutls-devel
%defattr(-, root, root)  

%{prefix}/include/xmlsec1/xmlsec/gnutls/*.h
%{prefix}/lib*/libxmlsec1-gnutls.*a
%{prefix}/lib*/pkgconfig/xmlsec1-gnutls.pc

%ifnarch ppc64
%files nss
%defattr(-, root, root)  

%{prefix}/lib*/libxmlsec1-nss.so.*
%{prefix}/lib*/libxmlsec1-nss.so

%files nss-devel
%defattr(-, root, root)  

%{prefix}/include/xmlsec1/xmlsec/nss/*.h
%{prefix}/lib*/libxmlsec1-nss.*a
%{prefix}/lib*/pkgconfig/xmlsec1-nss.pc
%endif

%changelog
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
