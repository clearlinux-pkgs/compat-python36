Name:           compat-python36
Version:        3.6.11
Release:        23
License:        Python-2.0
Summary:        The Python Programming Language
Url:            http://www.python.org
Group:          devel/python
Source0:        https://www.python.org/ftp/python/3.6.11/Python-3.6.11.tar.xz
Patch1:         0001-Fix-python-path-for-linux.patch
Patch2:         0002-Skip-tests-TODO-fix.patch
Patch3:         0003-Use-pybench-to-optimize-python.patch
Patch4:         0004-Add-avx2-and-avx512-support.patch
Patch5:         0005-stop-using-c99-as-flag-it-inhibits-FMA.patch
Patch6:         0006-add-AVX-versions-of-math-lib.patch
Patch7:         CVE-2019-9674.patch
Patch8:         CVE-2019-20907.patch

BuildRequires:  bzip2
BuildRequires:  db
BuildRequires:  grep
BuildRequires:  bzip2-dev
BuildRequires:  xz-dev
BuildRequires:  gdbm-dev
BuildRequires:  readline-dev
BuildRequires:  openssl
BuildRequires:  openssl-dev
BuildRequires:  sqlite-autoconf
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  libffi-dev
BuildRequires:  procps-ng-bin
BuildRequires:  netbase
Requires: compat-python36-core
Requires: compat-python36-lib
Requires: usrbinpython


%global __arch_install_post %{nil}

%description
The Python Programming Language.

%package lib
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description lib
The Python Programming Language.

%package lib-avx2
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python
Requires: 	compat-python36-lib

%description lib-avx2
The Python Programming Language.

%package core
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

Requires:  	openstack-setuptools-python3
Requires:  	openstack-setuptools-bin


%description core
The Python Programming Language.

%package dev
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel
Requires:       compat-python36-lib
Requires:       compat-python36-core
Requires:	usrbinpython

%define python_configure_flags  --with-threads --with-pymalloc  --without-cxx-main --with-signal-module --enable-ipv6=yes  --libdir=/usr/lib  ac_cv_header_bluetooth_bluetooth_h=no  ac_cv_header_bluetooth_h=no  --with-system-ffi --with-system-expat --with-lto=8 --with-computed-gotos


%description dev
The Python Programming Language.

%package doc
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description doc
The Python Programming Language.

%prep
%setup -q -n Python-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export LANG=C

# Build with PGO for perf improvement
export CFLAGS="$CFLAGS -O3"
%configure %python_configure_flags --enable-shared
make %{?_smp_mflags}

%install

%make_install
mv %{buildroot}/usr/lib/libpython*.so* %{buildroot}/usr/lib64/

%check
export LANG=C
#LD_LIBRARY_PATH=`pwd` ./python -Wd -E -tt  Lib/test/regrtest.py -v -x test_asyncio test_uuid test_subprocess || :


%files

%files lib
/usr/lib64/libpython3.6m.so.1.0

%files lib-avx2
%exclude /usr/lib64/haswell/libpython3.6m.so.1.0
%exclude /usr/lib64/haswell/libpython3.6m.so
#/usr/lib64/haswell/libpython3.so

%files core
%exclude /usr/bin/2to3
%exclude /usr/bin/2to3-3.6
%exclude /usr/bin/easy_install-3.6
%exclude /usr/bin/idle3
%exclude /usr/bin/idle3.6
%exclude /usr/bin/pip3
%exclude /usr/bin/pip3.6
%exclude /usr/bin/pydoc3
/usr/bin/pydoc3.6
%exclude /usr/bin/python3
%exclude /usr/bin/python3-config
/usr/bin/python3.6
/usr/bin/python3.6-config
/usr/bin/python3.6m
/usr/bin/python3.6m-config
%exclude /usr/bin/pyvenv
/usr/bin/pyvenv-3.6
/usr/lib/python3.6/
%exclude /usr/lib/python3.6/site-packages/pip
%exclude /usr/lib/python3.6/site-packages/setuptools-28.8.0.dist-info
%exclude /usr/lib/python3.6/site-packages/setuptools
%exclude /usr/lib/python3.6/ensurepip/_bundled/setuptools-28.8.0-py2.py3-none-any.whl
%exclude /usr/lib/python3.6/site-packages/pkg_resources
%exclude /usr/lib/python3.6/site-packages/easy_install.py
%exclude /usr/lib/python3.6/distutils/command/*.exe


%files dev
%exclude /usr/include/python3.6m/*.h
%exclude /usr/lib64/libpython3.so
%exclude /usr/lib64/libpython3.6m.so
%exclude /usr/lib64/pkgconfig/python3.pc
%exclude /usr/lib64/pkgconfig/python-3.6.pc
%exclude /usr/lib64/pkgconfig/python-3.6m.pc

%files doc
%exclude %{_mandir}/man1/*
