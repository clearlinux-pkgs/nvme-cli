#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v26
# autospec commit: 99a7985
#
Name     : nvme-cli
Version  : 2.14
Release  : 35
URL      : https://github.com/linux-nvme/nvme-cli/archive/v2.14/nvme-cli-2.14.tar.gz
Source0  : https://github.com/linux-nvme/nvme-cli/archive/v2.14/nvme-cli-2.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: nvme-cli-bin = %{version}-%{release}
Requires: nvme-cli-config = %{version}-%{release}
Requires: nvme-cli-data = %{version}-%{release}
Requires: nvme-cli-license = %{version}-%{release}
Requires: nvme-cli-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libnvme)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Kelly Kaoudis, kelly.n.kaoudis at intel.com, June 2015
Setting Up NVMe Tab Autocompletion for bash or zsh
==================================================

%package bin
Summary: bin components for the nvme-cli package.
Group: Binaries
Requires: nvme-cli-data = %{version}-%{release}
Requires: nvme-cli-config = %{version}-%{release}
Requires: nvme-cli-license = %{version}-%{release}
Requires: nvme-cli-services = %{version}-%{release}

%description bin
bin components for the nvme-cli package.


%package config
Summary: config components for the nvme-cli package.
Group: Default

%description config
config components for the nvme-cli package.


%package data
Summary: data components for the nvme-cli package.
Group: Data

%description data
data components for the nvme-cli package.


%package license
Summary: license components for the nvme-cli package.
Group: Default

%description license
license components for the nvme-cli package.


%package services
Summary: services components for the nvme-cli package.
Group: Systemd services
Requires: kmod
Requires: systemd

%description services
services components for the nvme-cli package.


%prep
%setup -q -n nvme-cli-2.14
cd %{_builddir}/nvme-cli-2.14
pushd ..
cp -a nvme-cli-2.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747762349
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/nvme-cli
cp %{_builddir}/nvme-cli-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/23a1f87d806ce0330b3d85485e399a5f9f553409 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/compiler/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/hash/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/htable/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/ilog/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/likely/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/nvme-cli-%{version}/ccan/ccan/typesafe_cb/LICENSE %{buildroot}/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/etc/nvme/discovery.conf
## install_append content
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/nvme
/usr/bin/nvme

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/65-persistent-net-nbft.rules
/usr/lib/udev/rules.d/70-nvmf-autoconnect.rules
/usr/lib/udev/rules.d/70-nvmf-keys.rules
/usr/lib/udev/rules.d/71-nvmf-netapp.rules
/usr/lib/udev/rules.d/71-nvmf-vastdata.rules

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/nvme
/usr/share/zsh/site-functions/_nvme

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nvme-cli/23a1f87d806ce0330b3d85485e399a5f9f553409
/usr/share/package-licenses/nvme-cli/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/nvme-cli/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/nvme-cli/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nvmefc-boot-connections.service
/usr/lib/systemd/system/nvmf-autoconnect.service
/usr/lib/systemd/system/nvmf-connect-nbft.service
/usr/lib/systemd/system/nvmf-connect.target
/usr/lib/systemd/system/nvmf-connect@.service
