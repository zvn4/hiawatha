Name:           hiawatha
Version:        VERSION
Release:        1%{?dist}
Summary:        Hiawatha, an advanced and secure webserver for Unix
Group:          Applications/Internet
License:        GPLv2
URL:            https://www.hiawatha-webserver.org/
Source0:        https://www.hiawatha-webserver.org/files/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  make,gcc,glibc-devel,libxml2-devel,libxslt-devel
Requires:       libxml2,libxslt

%description
Hiawatha is an advanced and secure webserver for Unix with the three key features: security, easy-to-use and lightweight.

%prep
%setup -q

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
cmake -DCMAKE_INSTALL_PREFIX="" -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
      -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
      -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DCMAKE_INSTALL_MANDIR=%{_mandir} \
      -DENABLE_TOMAHAWK=on -DENABLE_MONITOR=on
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_defaultdocdir}/hiawatha
cp ChangeLog %{buildroot}%{_defaultdocdir}/hiawatha
mkdir -p %{buildroot}%{_initrddir}
cp extra/debian/init.d/hiawatha %{buildroot}%{_initrddir}

%clean
rm -rf %{buildroot}

%files
%attr(-, root, root) %{_bindir}/
%attr(-, root, root) %{_sbindir}/
%attr(-, root, root) %{_libdir}/hiawatha/
%attr(-, root, root) %{_mandir}/
%attr(-, root, root) %{_sysconfdir}/hiawatha/
%attr(-, root, root) %{_localstatedir}/log/hiawatha/
%attr(-, root, root) %{_localstatedir}/www/hiawatha/
%attr(-, root, root) %{_defaultdocdir}/hiawatha/
%attr(-, root, root) %{_initrddir}/

%changelog