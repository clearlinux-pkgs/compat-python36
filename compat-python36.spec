Name:           compat-python36
Version:        3.6.5
Release:        5
License:        Python-2.0
Summary:        The Python Programming Language
Url:            http://www.python.org
Group:          devel/python
Source0:        https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
Patch0:         0001-Fix-python-path-for-linux.patch
# Causes test-suite failures
#Patch1:         0001-ensure-pip-upgrade.patch
Patch1:         skip-some-tests.patch
Patch2:         0001-Replace-getrandom-syscall-with-RDRAND-instruction.patch
Patch3:         pgo_profile_pybench.patch
Patch4:		avx2.patch
Patch5:		noentropy.patch
Patch6:		noc99.patch

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
Requires: compat-python3-core
Requires: compat-python3-lib
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
Requires: 	python3-lib

%description lib-avx2
The Python Programming Language.

%package core
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

Requires:  	setuptools-python3
Requires:  	setuptools-bin


%description core
The Python Programming Language.

%package dev
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel
Requires:       python3-lib
Requires:       python3-core
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
%patch0 -p1
# Todo fix these
%patch1 -p1
# make the code not block on getrandom during boot
#%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1

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




%files dev
%exclude /usr/include/python3.6m/*.h
%exclude /usr/lib64/libpython3.so
%exclude /usr/lib64/libpython3.6m.so
%exclude /usr/lib64/pkgconfig/python3.pc
%exclude /usr/lib64/pkgconfig/python-3.6.pc
%exclude /usr/lib64/pkgconfig/python-3.6m.pc

%files doc
%exclude %{_mandir}/man1/*
