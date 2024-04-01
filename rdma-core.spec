#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v7
# autospec commit: f56f1fa
#
%define keepstatic 1
Name     : rdma-core
Version  : 51.0
Release  : 62
URL      : https://github.com/linux-rdma/rdma-core/archive/v51.0/rdma-core-51.0.tar.gz
Source0  : https://github.com/linux-rdma/rdma-core/archive/v51.0/rdma-core-51.0.tar.gz
Summary  : RDMA core userspace libraries and daemons
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-2.0-only MIT
Requires: rdma-core-bin = %{version}-%{release}
Requires: rdma-core-config = %{version}-%{release}
Requires: rdma-core-data = %{version}-%{release}
Requires: rdma-core-lib = %{version}-%{release}
Requires: rdma-core-libexec = %{version}-%{release}
Requires: rdma-core-license = %{version}-%{release}
Requires: rdma-core-man = %{version}-%{release}
Requires: rdma-core-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libnl-dev
BuildRequires : pandoc
BuildRequires : pkg-config
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : pypi-cython
BuildRequires : pypi-docutils
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
RDMA core userspace infrastructure and documentation, including initialization
scripts, kernel driver-specific modprobe override configs, IPoIB network
scripts, dracut rules, and the rdma-ndd utility.

%package bin
Summary: bin components for the rdma-core package.
Group: Binaries
Requires: rdma-core-data = %{version}-%{release}
Requires: rdma-core-libexec = %{version}-%{release}
Requires: rdma-core-config = %{version}-%{release}
Requires: rdma-core-license = %{version}-%{release}
Requires: rdma-core-services = %{version}-%{release}

%description bin
bin components for the rdma-core package.


%package config
Summary: config components for the rdma-core package.
Group: Default

%description config
config components for the rdma-core package.


%package data
Summary: data components for the rdma-core package.
Group: Data

%description data
data components for the rdma-core package.


%package dev
Summary: dev components for the rdma-core package.
Group: Development
Requires: rdma-core-lib = %{version}-%{release}
Requires: rdma-core-bin = %{version}-%{release}
Requires: rdma-core-data = %{version}-%{release}
Provides: rdma-core-devel = %{version}-%{release}
Requires: rdma-core = %{version}-%{release}

%description dev
dev components for the rdma-core package.


%package doc
Summary: doc components for the rdma-core package.
Group: Documentation
Requires: rdma-core-man = %{version}-%{release}

%description doc
doc components for the rdma-core package.


%package lib
Summary: lib components for the rdma-core package.
Group: Libraries
Requires: rdma-core-data = %{version}-%{release}
Requires: rdma-core-libexec = %{version}-%{release}
Requires: rdma-core-license = %{version}-%{release}

%description lib
lib components for the rdma-core package.


%package libexec
Summary: libexec components for the rdma-core package.
Group: Default
Requires: rdma-core-config = %{version}-%{release}
Requires: rdma-core-license = %{version}-%{release}

%description libexec
libexec components for the rdma-core package.


%package license
Summary: license components for the rdma-core package.
Group: Default

%description license
license components for the rdma-core package.


%package man
Summary: man components for the rdma-core package.
Group: Default

%description man
man components for the rdma-core package.


%package services
Summary: services components for the rdma-core package.
Group: Systemd services
Requires: systemd

%description services
services components for the rdma-core package.


%package staticdev
Summary: staticdev components for the rdma-core package.
Group: Default
Requires: rdma-core-dev = %{version}-%{release}

%description staticdev
staticdev components for the rdma-core package.


%prep
%setup -q -n rdma-core-51.0
cd %{_builddir}/rdma-core-51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712004838
mkdir -p clr-build
pushd clr-build
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
%cmake .. -DCMAKE_INSTALL_SYSCONFDIR=/usr/share/defaults/rdma-core \
-DENABLE_STATIC=1
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DCMAKE_INSTALL_SYSCONFDIR=/usr/share/defaults/rdma-core \
-DENABLE_STATIC=1
make  %{?_smp_mflags}
popd

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
export SOURCE_DATE_EPOCH=1712004838
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rdma-core
cp %{_builddir}/rdma-core-%{version}/COPYING.BSD_FB %{buildroot}/usr/share/package-licenses/rdma-core/133cf03905c2dc7d8a061e1d6e9ced3117b0120f || :
cp %{_builddir}/rdma-core-%{version}/COPYING.BSD_MIT %{buildroot}/usr/share/package-licenses/rdma-core/de66bb2ca6b007504c1844178dce4e48ef2adfff || :
cp %{_builddir}/rdma-core-%{version}/COPYING.GPL2 %{buildroot}/usr/share/package-licenses/rdma-core/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/rdma-core-%{version}/ccan/LICENSE.CCO %{buildroot}/usr/share/package-licenses/rdma-core/eaff686ba07863809da758bed796270f84c877ec || :
cp %{_builddir}/rdma-core-%{version}/ccan/LICENSE.MIT %{buildroot}/usr/share/package-licenses/rdma-core/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/rdma-core-%{version}/providers/ipathverbs/COPYING %{buildroot}/usr/share/package-licenses/rdma-core/df75be21090fc8aa92d1175f31b7891432da3d09 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/libexec/truescale-serdes.cmds
rm -f %{buildroot}*/usr/share/defaults/rdma-core/init.d/ibacm
rm -f %{buildroot}*/usr/share/defaults/rdma-core/init.d/iwpmd
rm -f %{buildroot}*/usr/share/defaults/rdma-core/init.d/srpd
rm -f %{buildroot}*/usr/share/defaults/rdma-core/modprobe.d/mlx4.conf
rm -f %{buildroot}*/usr/share/defaults/rdma-core/modprobe.d/truescale.conf
rm -f %{buildroot}*/usr/share/defaults/rdma-core/srp_daemon.conf
rm -f %{buildroot}*/usr/share/defaults/rdma-core/udev/rules.d/70-persistent-ipoib.rules
## install_append content
pyver=$(pkg-config python3 --modversion)
rm -rf %{buildroot}*/usr/lib/python${pyver}
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib/udev/rdma_rename
/usr/lib/udev/rdma_rename

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cmtime
/V3/usr/bin/dump_fts
/V3/usr/bin/ib_acme
/V3/usr/bin/ibacm
/V3/usr/bin/ibaddr
/V3/usr/bin/ibcacheedit
/V3/usr/bin/ibccconfig
/V3/usr/bin/ibccquery
/V3/usr/bin/iblinkinfo
/V3/usr/bin/ibnetdiscover
/V3/usr/bin/ibping
/V3/usr/bin/ibportstate
/V3/usr/bin/ibqueryerrors
/V3/usr/bin/ibroute
/V3/usr/bin/ibstat
/V3/usr/bin/ibsysstat
/V3/usr/bin/ibtracert
/V3/usr/bin/ibv_asyncwatch
/V3/usr/bin/ibv_devices
/V3/usr/bin/ibv_devinfo
/V3/usr/bin/ibv_rc_pingpong
/V3/usr/bin/ibv_srq_pingpong
/V3/usr/bin/ibv_uc_pingpong
/V3/usr/bin/ibv_ud_pingpong
/V3/usr/bin/ibv_xsrq_pingpong
/V3/usr/bin/iwpmd
/V3/usr/bin/mckey
/V3/usr/bin/perfquery
/V3/usr/bin/rcopy
/V3/usr/bin/rdma-ndd
/V3/usr/bin/rdma_client
/V3/usr/bin/rdma_server
/V3/usr/bin/rdma_xclient
/V3/usr/bin/rdma_xserver
/V3/usr/bin/riostream
/V3/usr/bin/rping
/V3/usr/bin/rstream
/V3/usr/bin/saquery
/V3/usr/bin/sminfo
/V3/usr/bin/smpdump
/V3/usr/bin/smpquery
/V3/usr/bin/srp_daemon
/V3/usr/bin/ucmatose
/V3/usr/bin/udaddy
/V3/usr/bin/udpong
/V3/usr/bin/vendstat
/usr/bin/check_lft_balance.pl
/usr/bin/cmtime
/usr/bin/dump_fts
/usr/bin/dump_lfts.sh
/usr/bin/dump_mfts.sh
/usr/bin/ib_acme
/usr/bin/ibacm
/usr/bin/ibaddr
/usr/bin/ibcacheedit
/usr/bin/ibccconfig
/usr/bin/ibccquery
/usr/bin/ibfindnodesusing.pl
/usr/bin/ibhosts
/usr/bin/ibidsverify.pl
/usr/bin/iblinkinfo
/usr/bin/ibnetdiscover
/usr/bin/ibnodes
/usr/bin/ibping
/usr/bin/ibportstate
/usr/bin/ibqueryerrors
/usr/bin/ibroute
/usr/bin/ibrouters
/usr/bin/ibsrpdm
/usr/bin/ibstat
/usr/bin/ibstatus
/usr/bin/ibswitches
/usr/bin/ibsysstat
/usr/bin/ibtracert
/usr/bin/ibv_asyncwatch
/usr/bin/ibv_devices
/usr/bin/ibv_devinfo
/usr/bin/ibv_rc_pingpong
/usr/bin/ibv_srq_pingpong
/usr/bin/ibv_uc_pingpong
/usr/bin/ibv_ud_pingpong
/usr/bin/ibv_xsrq_pingpong
/usr/bin/iwpmd
/usr/bin/mckey
/usr/bin/perfquery
/usr/bin/rcopy
/usr/bin/rdma-ndd
/usr/bin/rdma_client
/usr/bin/rdma_server
/usr/bin/rdma_xclient
/usr/bin/rdma_xserver
/usr/bin/riostream
/usr/bin/rping
/usr/bin/rstream
/usr/bin/run_srp_daemon
/usr/bin/saquery
/usr/bin/sminfo
/usr/bin/smpdump
/usr/bin/smpquery
/usr/bin/srp_daemon
/usr/bin/srp_daemon.sh
/usr/bin/ucmatose
/usr/bin/udaddy
/usr/bin/udpong
/usr/bin/vendstat

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/60-rdma-ndd.rules
/usr/lib/udev/rules.d/60-rdma-persistent-naming.rules
/usr/lib/udev/rules.d/60-srp_daemon.rules
/usr/lib/udev/rules.d/75-rdma-description.rules
/usr/lib/udev/rules.d/90-iwpmd.rules
/usr/lib/udev/rules.d/90-rdma-hw-modules.rules
/usr/lib/udev/rules.d/90-rdma-ulp-modules.rules
/usr/lib/udev/rules.d/90-rdma-umad.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/rdma-core/infiniband-diags/error_thresholds
/usr/share/defaults/rdma-core/infiniband-diags/ibdiag.conf
/usr/share/defaults/rdma-core/iwpmd.conf
/usr/share/defaults/rdma-core/libibverbs.d/bnxt_re.driver
/usr/share/defaults/rdma-core/libibverbs.d/cxgb4.driver
/usr/share/defaults/rdma-core/libibverbs.d/efa.driver
/usr/share/defaults/rdma-core/libibverbs.d/erdma.driver
/usr/share/defaults/rdma-core/libibverbs.d/hfi1verbs.driver
/usr/share/defaults/rdma-core/libibverbs.d/hns.driver
/usr/share/defaults/rdma-core/libibverbs.d/ipathverbs.driver
/usr/share/defaults/rdma-core/libibverbs.d/irdma.driver
/usr/share/defaults/rdma-core/libibverbs.d/mana.driver
/usr/share/defaults/rdma-core/libibverbs.d/mlx4.driver
/usr/share/defaults/rdma-core/libibverbs.d/mlx5.driver
/usr/share/defaults/rdma-core/libibverbs.d/mthca.driver
/usr/share/defaults/rdma-core/libibverbs.d/ocrdma.driver
/usr/share/defaults/rdma-core/libibverbs.d/qedr.driver
/usr/share/defaults/rdma-core/libibverbs.d/rxe.driver
/usr/share/defaults/rdma-core/libibverbs.d/siw.driver
/usr/share/defaults/rdma-core/libibverbs.d/vmw_pvrdma.driver
/usr/share/defaults/rdma-core/rdma/modules/infiniband.conf
/usr/share/defaults/rdma-core/rdma/modules/iwarp.conf
/usr/share/defaults/rdma-core/rdma/modules/iwpmd.conf
/usr/share/defaults/rdma-core/rdma/modules/opa.conf
/usr/share/defaults/rdma-core/rdma/modules/rdma.conf
/usr/share/defaults/rdma-core/rdma/modules/roce.conf
/usr/share/defaults/rdma-core/rdma/modules/srp_daemon.conf
/usr/share/perl5/IBswcountlimits.pm

%files dev
%defattr(-,root,root,-)
/usr/include/infiniband/acm.h
/usr/include/infiniband/acm_prov.h
/usr/include/infiniband/arch.h
/usr/include/infiniband/efadv.h
/usr/include/infiniband/hnsdv.h
/usr/include/infiniband/ib.h
/usr/include/infiniband/ib_user_ioctl_verbs.h
/usr/include/infiniband/ibnetdisc.h
/usr/include/infiniband/ibnetdisc_osd.h
/usr/include/infiniband/mad.h
/usr/include/infiniband/mad_osd.h
/usr/include/infiniband/manadv.h
/usr/include/infiniband/mlx4dv.h
/usr/include/infiniband/mlx5_api.h
/usr/include/infiniband/mlx5_user_ioctl_verbs.h
/usr/include/infiniband/mlx5dv.h
/usr/include/infiniband/opcode.h
/usr/include/infiniband/sa-kern-abi.h
/usr/include/infiniband/sa.h
/usr/include/infiniband/tm_types.h
/usr/include/infiniband/umad.h
/usr/include/infiniband/umad_cm.h
/usr/include/infiniband/umad_sa.h
/usr/include/infiniband/umad_sa_mcm.h
/usr/include/infiniband/umad_sm.h
/usr/include/infiniband/umad_str.h
/usr/include/infiniband/umad_types.h
/usr/include/infiniband/verbs.h
/usr/include/infiniband/verbs_api.h
/usr/include/rdma/rdma_cma.h
/usr/include/rdma/rdma_cma_abi.h
/usr/include/rdma/rdma_verbs.h
/usr/include/rdma/rsocket.h
/usr/lib64/libefa.so
/usr/lib64/libhns.so
/usr/lib64/libibmad.so
/usr/lib64/libibnetdisc.so
/usr/lib64/libibumad.so
/usr/lib64/libibverbs.so
/usr/lib64/libmana.so
/usr/lib64/libmlx4.so
/usr/lib64/libmlx5.so
/usr/lib64/librdmacm.so
/usr/lib64/pkgconfig/libefa.pc
/usr/lib64/pkgconfig/libhns.pc
/usr/lib64/pkgconfig/libibmad.pc
/usr/lib64/pkgconfig/libibnetdisc.pc
/usr/lib64/pkgconfig/libibumad.pc
/usr/lib64/pkgconfig/libibverbs.pc
/usr/lib64/pkgconfig/libmana.pc
/usr/lib64/pkgconfig/libmlx4.pc
/usr/lib64/pkgconfig/libmlx5.pc
/usr/lib64/pkgconfig/librdmacm.pc
/usr/share/man/man3/efadv_create_driver_qp.3
/usr/share/man/man3/efadv_create_qp_ex.3
/usr/share/man/man3/efadv_query_ah.3
/usr/share/man/man3/efadv_query_device.3
/usr/share/man/man3/efadv_query_mr.3
/usr/share/man/man3/hnsdv_create_qp.3
/usr/share/man/man3/hnsdv_is_supported.3
/usr/share/man/man3/hnsdv_query_device.3
/usr/share/man/man3/ibnd_debug.3
/usr/share/man/man3/ibnd_destroy_fabric.3
/usr/share/man/man3/ibnd_discover_fabric.3
/usr/share/man/man3/ibnd_find_node_dr.3
/usr/share/man/man3/ibnd_find_node_guid.3
/usr/share/man/man3/ibnd_iter_nodes.3
/usr/share/man/man3/ibnd_iter_nodes_type.3
/usr/share/man/man3/ibnd_set_max_smps_on_wire.3
/usr/share/man/man3/ibnd_show_progress.3
/usr/share/man/man3/ibv_ack_async_event.3
/usr/share/man/man3/ibv_ack_cq_events.3
/usr/share/man/man3/ibv_advise_mr.3
/usr/share/man/man3/ibv_alloc_dm.3
/usr/share/man/man3/ibv_alloc_mw.3
/usr/share/man/man3/ibv_alloc_null_mr.3
/usr/share/man/man3/ibv_alloc_parent_domain.3
/usr/share/man/man3/ibv_alloc_pd.3
/usr/share/man/man3/ibv_alloc_td.3
/usr/share/man/man3/ibv_attach_counters_point_flow.3
/usr/share/man/man3/ibv_attach_mcast.3
/usr/share/man/man3/ibv_bind_mw.3
/usr/share/man/man3/ibv_close_device.3
/usr/share/man/man3/ibv_close_xrcd.3
/usr/share/man/man3/ibv_create_ah.3
/usr/share/man/man3/ibv_create_ah_from_wc.3
/usr/share/man/man3/ibv_create_comp_channel.3
/usr/share/man/man3/ibv_create_counters.3
/usr/share/man/man3/ibv_create_cq.3
/usr/share/man/man3/ibv_create_cq_ex.3
/usr/share/man/man3/ibv_create_flow.3
/usr/share/man/man3/ibv_create_flow_action.3
/usr/share/man/man3/ibv_create_qp.3
/usr/share/man/man3/ibv_create_qp_ex.3
/usr/share/man/man3/ibv_create_rwq_ind_table.3
/usr/share/man/man3/ibv_create_srq.3
/usr/share/man/man3/ibv_create_srq_ex.3
/usr/share/man/man3/ibv_create_wq.3
/usr/share/man/man3/ibv_dealloc_mw.3
/usr/share/man/man3/ibv_dealloc_pd.3
/usr/share/man/man3/ibv_dealloc_td.3
/usr/share/man/man3/ibv_dereg_mr.3
/usr/share/man/man3/ibv_destroy_ah.3
/usr/share/man/man3/ibv_destroy_comp_channel.3
/usr/share/man/man3/ibv_destroy_counters.3
/usr/share/man/man3/ibv_destroy_cq.3
/usr/share/man/man3/ibv_destroy_flow.3
/usr/share/man/man3/ibv_destroy_flow_action.3
/usr/share/man/man3/ibv_destroy_qp.3
/usr/share/man/man3/ibv_destroy_rwq_ind_table.3
/usr/share/man/man3/ibv_destroy_srq.3
/usr/share/man/man3/ibv_destroy_wq.3
/usr/share/man/man3/ibv_detach_mcast.3
/usr/share/man/man3/ibv_event_type_str.3
/usr/share/man/man3/ibv_fork_init.3
/usr/share/man/man3/ibv_free_device_list.3
/usr/share/man/man3/ibv_free_dm.3
/usr/share/man/man3/ibv_get_async_event.3
/usr/share/man/man3/ibv_get_cq_event.3
/usr/share/man/man3/ibv_get_device_guid.3
/usr/share/man/man3/ibv_get_device_index.3
/usr/share/man/man3/ibv_get_device_list.3
/usr/share/man/man3/ibv_get_device_name.3
/usr/share/man/man3/ibv_get_pkey_index.3
/usr/share/man/man3/ibv_get_srq_num.3
/usr/share/man/man3/ibv_import_device.3
/usr/share/man/man3/ibv_import_dm.3
/usr/share/man/man3/ibv_import_mr.3
/usr/share/man/man3/ibv_import_pd.3
/usr/share/man/man3/ibv_inc_rkey.3
/usr/share/man/man3/ibv_init_ah_from_wc.3
/usr/share/man/man3/ibv_is_fork_initialized.3
/usr/share/man/man3/ibv_memcpy_from_dm.3
/usr/share/man/man3/ibv_memcpy_to_dm.3
/usr/share/man/man3/ibv_modify_cq.3
/usr/share/man/man3/ibv_modify_flow_action.3
/usr/share/man/man3/ibv_modify_qp.3
/usr/share/man/man3/ibv_modify_qp_rate_limit.3
/usr/share/man/man3/ibv_modify_srq.3
/usr/share/man/man3/ibv_modify_wq.3
/usr/share/man/man3/ibv_node_type_str.3
/usr/share/man/man3/ibv_open_device.3
/usr/share/man/man3/ibv_open_qp.3
/usr/share/man/man3/ibv_open_xrcd.3
/usr/share/man/man3/ibv_poll_cq.3
/usr/share/man/man3/ibv_port_state_str.3
/usr/share/man/man3/ibv_post_recv.3
/usr/share/man/man3/ibv_post_send.3
/usr/share/man/man3/ibv_post_srq_ops.3
/usr/share/man/man3/ibv_post_srq_recv.3
/usr/share/man/man3/ibv_query_device.3
/usr/share/man/man3/ibv_query_device_ex.3
/usr/share/man/man3/ibv_query_ece.3
/usr/share/man/man3/ibv_query_gid.3
/usr/share/man/man3/ibv_query_gid_ex.3
/usr/share/man/man3/ibv_query_gid_table.3
/usr/share/man/man3/ibv_query_pkey.3
/usr/share/man/man3/ibv_query_port.3
/usr/share/man/man3/ibv_query_qp.3
/usr/share/man/man3/ibv_query_qp_data_in_order.3
/usr/share/man/man3/ibv_query_rt_values_ex.3
/usr/share/man/man3/ibv_query_srq.3
/usr/share/man/man3/ibv_rate_to_mbps.3
/usr/share/man/man3/ibv_rate_to_mult.3
/usr/share/man/man3/ibv_read_counters.3
/usr/share/man/man3/ibv_reg_dm_mr.3
/usr/share/man/man3/ibv_reg_mr.3
/usr/share/man/man3/ibv_req_notify_cq.3
/usr/share/man/man3/ibv_rereg_mr.3
/usr/share/man/man3/ibv_resize_cq.3
/usr/share/man/man3/ibv_set_ece.3
/usr/share/man/man3/ibv_unimport_dm.3
/usr/share/man/man3/ibv_unimport_mr.3
/usr/share/man/man3/ibv_unimport_pd.3
/usr/share/man/man3/ibv_wr_abort.3
/usr/share/man/man3/ibv_wr_atomic_cmp_swp.3
/usr/share/man/man3/ibv_wr_atomic_fetch_add.3
/usr/share/man/man3/ibv_wr_bind_mw.3
/usr/share/man/man3/ibv_wr_complete.3
/usr/share/man/man3/ibv_wr_flush.3
/usr/share/man/man3/ibv_wr_local_inv.3
/usr/share/man/man3/ibv_wr_post.3
/usr/share/man/man3/ibv_wr_rdma_read.3
/usr/share/man/man3/ibv_wr_rdma_write.3
/usr/share/man/man3/ibv_wr_rdma_write_imm.3
/usr/share/man/man3/ibv_wr_send.3
/usr/share/man/man3/ibv_wr_send_imm.3
/usr/share/man/man3/ibv_wr_send_inv.3
/usr/share/man/man3/ibv_wr_send_tso.3
/usr/share/man/man3/ibv_wr_set_inline_data.3
/usr/share/man/man3/ibv_wr_set_inline_data_list.3
/usr/share/man/man3/ibv_wr_set_sge.3
/usr/share/man/man3/ibv_wr_set_sge_list.3
/usr/share/man/man3/ibv_wr_set_ud_addr.3
/usr/share/man/man3/ibv_wr_set_xrc_srqn.3
/usr/share/man/man3/ibv_wr_start.3
/usr/share/man/man3/manadv_init_obj.3
/usr/share/man/man3/manadv_set_context_attr.3
/usr/share/man/man3/mbps_to_ibv_rate.3
/usr/share/man/man3/mlx4dv_init_obj.3
/usr/share/man/man3/mlx4dv_query_device.3
/usr/share/man/man3/mlx4dv_set_context_attr.3
/usr/share/man/man3/mlx5dv_alloc_dm.3
/usr/share/man/man3/mlx5dv_alloc_var.3
/usr/share/man/man3/mlx5dv_create_cq.3
/usr/share/man/man3/mlx5dv_create_flow.3
/usr/share/man/man3/mlx5dv_create_flow_action_modify_header.3
/usr/share/man/man3/mlx5dv_create_flow_action_packet_reformat.3
/usr/share/man/man3/mlx5dv_create_flow_matcher.3
/usr/share/man/man3/mlx5dv_create_mkey.3
/usr/share/man/man3/mlx5dv_create_qp.3
/usr/share/man/man3/mlx5dv_create_steering_anchor.3
/usr/share/man/man3/mlx5dv_crypto_login.3
/usr/share/man/man3/mlx5dv_crypto_login_create.3
/usr/share/man/man3/mlx5dv_crypto_login_destroy.3
/usr/share/man/man3/mlx5dv_crypto_login_query.3
/usr/share/man/man3/mlx5dv_crypto_login_query_state.3
/usr/share/man/man3/mlx5dv_crypto_logout.3
/usr/share/man/man3/mlx5dv_dci_stream_id_reset.3
/usr/share/man/man3/mlx5dv_dek_create.3
/usr/share/man/man3/mlx5dv_dek_destroy.3
/usr/share/man/man3/mlx5dv_dek_query.3
/usr/share/man/man3/mlx5dv_destroy_mkey.3
/usr/share/man/man3/mlx5dv_destroy_steering_anchor.3
/usr/share/man/man3/mlx5dv_devx_alloc_msi_vector.3
/usr/share/man/man3/mlx5dv_devx_alloc_uar.3
/usr/share/man/man3/mlx5dv_devx_cq_modify.3
/usr/share/man/man3/mlx5dv_devx_cq_query.3
/usr/share/man/man3/mlx5dv_devx_create_cmd_comp.3
/usr/share/man/man3/mlx5dv_devx_create_eq.3
/usr/share/man/man3/mlx5dv_devx_create_event_channel.3
/usr/share/man/man3/mlx5dv_devx_destroy_cmd_comp.3
/usr/share/man/man3/mlx5dv_devx_destroy_eq.3
/usr/share/man/man3/mlx5dv_devx_destroy_event_channel.3
/usr/share/man/man3/mlx5dv_devx_free_msi_vector.3
/usr/share/man/man3/mlx5dv_devx_free_uar.3
/usr/share/man/man3/mlx5dv_devx_general_cmd.3
/usr/share/man/man3/mlx5dv_devx_get_async_cmd_comp.3
/usr/share/man/man3/mlx5dv_devx_get_event.3
/usr/share/man/man3/mlx5dv_devx_ind_tbl_modify.3
/usr/share/man/man3/mlx5dv_devx_ind_tbl_query.3
/usr/share/man/man3/mlx5dv_devx_obj_create.3
/usr/share/man/man3/mlx5dv_devx_obj_destroy.3
/usr/share/man/man3/mlx5dv_devx_obj_modify.3
/usr/share/man/man3/mlx5dv_devx_obj_query.3
/usr/share/man/man3/mlx5dv_devx_obj_query_async.3
/usr/share/man/man3/mlx5dv_devx_qp_modify.3
/usr/share/man/man3/mlx5dv_devx_qp_query.3
/usr/share/man/man3/mlx5dv_devx_query_eqn.3
/usr/share/man/man3/mlx5dv_devx_srq_modify.3
/usr/share/man/man3/mlx5dv_devx_srq_query.3
/usr/share/man/man3/mlx5dv_devx_subscribe_devx_event.3
/usr/share/man/man3/mlx5dv_devx_subscribe_devx_event_fd.3
/usr/share/man/man3/mlx5dv_devx_umem_dereg.3
/usr/share/man/man3/mlx5dv_devx_umem_reg.3
/usr/share/man/man3/mlx5dv_devx_umem_reg_ex.3
/usr/share/man/man3/mlx5dv_devx_wq_modify.3
/usr/share/man/man3/mlx5dv_devx_wq_query.3
/usr/share/man/man3/mlx5dv_dm_map_op_addr.3
/usr/share/man/man3/mlx5dv_dr_action_create_aso.3
/usr/share/man/man3/mlx5dv_dr_action_create_default_miss.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_array.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_devx_tir.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_ib_port.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_ibv_qp.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_root_table.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_table.3
/usr/share/man/man3/mlx5dv_dr_action_create_dest_vport.3
/usr/share/man/man3/mlx5dv_dr_action_create_drop.3
/usr/share/man/man3/mlx5dv_dr_action_create_flow_counter.3
/usr/share/man/man3/mlx5dv_dr_action_create_flow_meter.3
/usr/share/man/man3/mlx5dv_dr_action_create_flow_sampler.3
/usr/share/man/man3/mlx5dv_dr_action_create_modify_header.3
/usr/share/man/man3/mlx5dv_dr_action_create_packet_reformat.3
/usr/share/man/man3/mlx5dv_dr_action_create_pop_vlan.3
/usr/share/man/man3/mlx5dv_dr_action_create_push_vlan.3
/usr/share/man/man3/mlx5dv_dr_action_create_tag.3
/usr/share/man/man3/mlx5dv_dr_action_destroy.3
/usr/share/man/man3/mlx5dv_dr_action_modify_aso.3
/usr/share/man/man3/mlx5dv_dr_action_modify_flow_meter.3
/usr/share/man/man3/mlx5dv_dr_aso_other_domain_link.3
/usr/share/man/man3/mlx5dv_dr_aso_other_domain_unlink.3
/usr/share/man/man3/mlx5dv_dr_domain_allow_duplicate_rules.3
/usr/share/man/man3/mlx5dv_dr_domain_create.3
/usr/share/man/man3/mlx5dv_dr_domain_destroy.3
/usr/share/man/man3/mlx5dv_dr_domain_set_reclaim_device_memory.3
/usr/share/man/man3/mlx5dv_dr_domain_sync.3
/usr/share/man/man3/mlx5dv_dr_flow.3
/usr/share/man/man3/mlx5dv_dr_matcher_create.3
/usr/share/man/man3/mlx5dv_dr_matcher_destroy.3
/usr/share/man/man3/mlx5dv_dr_matcher_set_layout.3
/usr/share/man/man3/mlx5dv_dr_rule_create.3
/usr/share/man/man3/mlx5dv_dr_rule_destroy.3
/usr/share/man/man3/mlx5dv_dr_table_create.3
/usr/share/man/man3/mlx5dv_dr_table_destroy.3
/usr/share/man/man3/mlx5dv_dump.3
/usr/share/man/man3/mlx5dv_dump_dr_domain.3
/usr/share/man/man3/mlx5dv_dump_dr_matcher.3
/usr/share/man/man3/mlx5dv_dump_dr_rule.3
/usr/share/man/man3/mlx5dv_dump_dr_table.3
/usr/share/man/man3/mlx5dv_flow_action_esp.3
/usr/share/man/man3/mlx5dv_free_var.3
/usr/share/man/man3/mlx5dv_get_clock_info.3
/usr/share/man/man3/mlx5dv_get_vfio_device_list.3
/usr/share/man/man3/mlx5dv_init_obj.3
/usr/share/man/man3/mlx5dv_is_supported.3
/usr/share/man/man3/mlx5dv_map_ah_to_qp.3
/usr/share/man/man3/mlx5dv_mkey_check.3
/usr/share/man/man3/mlx5dv_modify_qp_lag_port.3
/usr/share/man/man3/mlx5dv_modify_qp_sched_elem.3
/usr/share/man/man3/mlx5dv_modify_qp_udp_sport.3
/usr/share/man/man3/mlx5dv_open_device.3
/usr/share/man/man3/mlx5dv_pp_alloc.3
/usr/share/man/man3/mlx5dv_pp_free.3
/usr/share/man/man3/mlx5dv_qp_cancel_posted_send_wrs.3
/usr/share/man/man3/mlx5dv_qp_ex_from_ibv_qp_ex.3
/usr/share/man/man3/mlx5dv_query_device.3
/usr/share/man/man3/mlx5dv_query_port.3
/usr/share/man/man3/mlx5dv_query_qp_lag_port.3
/usr/share/man/man3/mlx5dv_reserved_qpn_alloc.3
/usr/share/man/man3/mlx5dv_reserved_qpn_dealloc.3
/usr/share/man/man3/mlx5dv_sched_leaf_create.3
/usr/share/man/man3/mlx5dv_sched_leaf_destroy.3
/usr/share/man/man3/mlx5dv_sched_leaf_modify.3
/usr/share/man/man3/mlx5dv_sched_node_create.3
/usr/share/man/man3/mlx5dv_sched_node_destroy.3
/usr/share/man/man3/mlx5dv_sched_node_modify.3
/usr/share/man/man3/mlx5dv_ts_to_ns.3
/usr/share/man/man3/mlx5dv_vfio_get_events_fd.3
/usr/share/man/man3/mlx5dv_vfio_process_events.3
/usr/share/man/man3/mlx5dv_wr_memcpy.3
/usr/share/man/man3/mlx5dv_wr_mkey_configure.3
/usr/share/man/man3/mlx5dv_wr_mr_interleaved.3
/usr/share/man/man3/mlx5dv_wr_mr_list.3
/usr/share/man/man3/mlx5dv_wr_post.3
/usr/share/man/man3/mlx5dv_wr_raw_wqe.3
/usr/share/man/man3/mlx5dv_wr_set_dc_addr.3
/usr/share/man/man3/mlx5dv_wr_set_dc_addr_stream.3
/usr/share/man/man3/mlx5dv_wr_set_mkey_access_flags.3
/usr/share/man/man3/mlx5dv_wr_set_mkey_crypto.3
/usr/share/man/man3/mlx5dv_wr_set_mkey_layout_interleaved.3
/usr/share/man/man3/mlx5dv_wr_set_mkey_layout_list.3
/usr/share/man/man3/mlx5dv_wr_set_mkey_sig_block.3
/usr/share/man/man3/mult_to_ibv_rate.3
/usr/share/man/man3/rdma_accept.3
/usr/share/man/man3/rdma_ack_cm_event.3
/usr/share/man/man3/rdma_bind_addr.3
/usr/share/man/man3/rdma_connect.3
/usr/share/man/man3/rdma_create_ep.3
/usr/share/man/man3/rdma_create_event_channel.3
/usr/share/man/man3/rdma_create_id.3
/usr/share/man/man3/rdma_create_qp.3
/usr/share/man/man3/rdma_create_srq.3
/usr/share/man/man3/rdma_dereg_mr.3
/usr/share/man/man3/rdma_destroy_ep.3
/usr/share/man/man3/rdma_destroy_event_channel.3
/usr/share/man/man3/rdma_destroy_id.3
/usr/share/man/man3/rdma_destroy_qp.3
/usr/share/man/man3/rdma_destroy_srq.3
/usr/share/man/man3/rdma_disconnect.3
/usr/share/man/man3/rdma_establish.3
/usr/share/man/man3/rdma_event_str.3
/usr/share/man/man3/rdma_free_devices.3
/usr/share/man/man3/rdma_get_cm_event.3
/usr/share/man/man3/rdma_get_devices.3
/usr/share/man/man3/rdma_get_dst_port.3
/usr/share/man/man3/rdma_get_local_addr.3
/usr/share/man/man3/rdma_get_peer_addr.3
/usr/share/man/man3/rdma_get_recv_comp.3
/usr/share/man/man3/rdma_get_remote_ece.3
/usr/share/man/man3/rdma_get_request.3
/usr/share/man/man3/rdma_get_send_comp.3
/usr/share/man/man3/rdma_get_src_port.3
/usr/share/man/man3/rdma_getaddrinfo.3
/usr/share/man/man3/rdma_init_qp_attr.3
/usr/share/man/man3/rdma_join_multicast.3
/usr/share/man/man3/rdma_join_multicast_ex.3
/usr/share/man/man3/rdma_leave_multicast.3
/usr/share/man/man3/rdma_listen.3
/usr/share/man/man3/rdma_migrate_id.3
/usr/share/man/man3/rdma_notify.3
/usr/share/man/man3/rdma_post_read.3
/usr/share/man/man3/rdma_post_readv.3
/usr/share/man/man3/rdma_post_recv.3
/usr/share/man/man3/rdma_post_recvv.3
/usr/share/man/man3/rdma_post_send.3
/usr/share/man/man3/rdma_post_sendv.3
/usr/share/man/man3/rdma_post_ud_send.3
/usr/share/man/man3/rdma_post_write.3
/usr/share/man/man3/rdma_post_writev.3
/usr/share/man/man3/rdma_reg_msgs.3
/usr/share/man/man3/rdma_reg_read.3
/usr/share/man/man3/rdma_reg_write.3
/usr/share/man/man3/rdma_reject.3
/usr/share/man/man3/rdma_resolve_addr.3
/usr/share/man/man3/rdma_resolve_route.3
/usr/share/man/man3/rdma_set_local_ece.3
/usr/share/man/man3/rdma_set_option.3
/usr/share/man/man3/umad_addr_dump.3
/usr/share/man/man3/umad_alloc.3
/usr/share/man/man3/umad_attribute_str.3
/usr/share/man/man3/umad_class_str.3
/usr/share/man/man3/umad_close_port.3
/usr/share/man/man3/umad_debug.3
/usr/share/man/man3/umad_done.3
/usr/share/man/man3/umad_dump.3
/usr/share/man/man3/umad_free.3
/usr/share/man/man3/umad_get_ca.3
/usr/share/man/man3/umad_get_ca_portguids.3
/usr/share/man/man3/umad_get_cas_names.3
/usr/share/man/man3/umad_get_fd.3
/usr/share/man/man3/umad_get_issm_path.3
/usr/share/man/man3/umad_get_mad.3
/usr/share/man/man3/umad_get_mad_addr.3
/usr/share/man/man3/umad_get_pkey.3
/usr/share/man/man3/umad_get_port.3
/usr/share/man/man3/umad_init.3
/usr/share/man/man3/umad_mad_status_str.3
/usr/share/man/man3/umad_method_str.3
/usr/share/man/man3/umad_open_port.3
/usr/share/man/man3/umad_poll.3
/usr/share/man/man3/umad_recv.3
/usr/share/man/man3/umad_register.3
/usr/share/man/man3/umad_register2.3
/usr/share/man/man3/umad_register_oui.3
/usr/share/man/man3/umad_release_ca.3
/usr/share/man/man3/umad_release_port.3
/usr/share/man/man3/umad_send.3
/usr/share/man/man3/umad_set_addr.3
/usr/share/man/man3/umad_set_addr_net.3
/usr/share/man/man3/umad_set_grh.3
/usr/share/man/man3/umad_set_grh_net.3
/usr/share/man/man3/umad_set_pkey.3
/usr/share/man/man3/umad_size.3
/usr/share/man/man3/umad_status.3
/usr/share/man/man3/umad_unregister.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/rdma\-core/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/ibacm/libibacmp.so
/V3/usr/lib64/libefa.so.1.3.51.0
/V3/usr/lib64/libhns.so.1.0.51.0
/V3/usr/lib64/libibmad.so.5.3.51.0
/V3/usr/lib64/libibnetdisc.so.5.1.51.0
/V3/usr/lib64/libibumad.so.3.2.51.0
/V3/usr/lib64/libibverbs.so.1.14.51.0
/V3/usr/lib64/libibverbs/libbnxt_re-rdmav34.so
/V3/usr/lib64/libibverbs/libcxgb4-rdmav34.so
/V3/usr/lib64/libibverbs/liberdma-rdmav34.so
/V3/usr/lib64/libibverbs/libhfi1verbs-rdmav34.so
/V3/usr/lib64/libibverbs/libipathverbs-rdmav34.so
/V3/usr/lib64/libibverbs/libirdma-rdmav34.so
/V3/usr/lib64/libibverbs/libmthca-rdmav34.so
/V3/usr/lib64/libibverbs/libocrdma-rdmav34.so
/V3/usr/lib64/libibverbs/libqedr-rdmav34.so
/V3/usr/lib64/libibverbs/librxe-rdmav34.so
/V3/usr/lib64/libibverbs/libsiw-rdmav34.so
/V3/usr/lib64/libibverbs/libvmw_pvrdma-rdmav34.so
/V3/usr/lib64/libmana.so.1.0.51.0
/V3/usr/lib64/libmlx4.so.1.0.51.0
/V3/usr/lib64/libmlx5.so.1.24.51.0
/V3/usr/lib64/librdmacm.so.1.3.51.0
/V3/usr/lib64/rsocket/librspreload.so
/usr/lib64/ibacm/libibacmp.so
/usr/lib64/libefa.so.1
/usr/lib64/libefa.so.1.3.51.0
/usr/lib64/libhns.so.1
/usr/lib64/libhns.so.1.0.51.0
/usr/lib64/libibmad.so.5
/usr/lib64/libibmad.so.5.3.51.0
/usr/lib64/libibnetdisc.so.5
/usr/lib64/libibnetdisc.so.5.1.51.0
/usr/lib64/libibumad.so.3
/usr/lib64/libibumad.so.3.2.51.0
/usr/lib64/libibverbs.so.1
/usr/lib64/libibverbs.so.1.14.51.0
/usr/lib64/libibverbs/libbnxt_re-rdmav34.so
/usr/lib64/libibverbs/libcxgb4-rdmav34.so
/usr/lib64/libibverbs/libefa-rdmav34.so
/usr/lib64/libibverbs/liberdma-rdmav34.so
/usr/lib64/libibverbs/libhfi1verbs-rdmav34.so
/usr/lib64/libibverbs/libhns-rdmav34.so
/usr/lib64/libibverbs/libipathverbs-rdmav34.so
/usr/lib64/libibverbs/libirdma-rdmav34.so
/usr/lib64/libibverbs/libmana-rdmav34.so
/usr/lib64/libibverbs/libmlx4-rdmav34.so
/usr/lib64/libibverbs/libmlx5-rdmav34.so
/usr/lib64/libibverbs/libmthca-rdmav34.so
/usr/lib64/libibverbs/libocrdma-rdmav34.so
/usr/lib64/libibverbs/libqedr-rdmav34.so
/usr/lib64/libibverbs/librxe-rdmav34.so
/usr/lib64/libibverbs/libsiw-rdmav34.so
/usr/lib64/libibverbs/libvmw_pvrdma-rdmav34.so
/usr/lib64/libmana.so.1
/usr/lib64/libmana.so.1.0.51.0
/usr/lib64/libmlx4.so.1
/usr/lib64/libmlx4.so.1.0.51.0
/usr/lib64/libmlx5.so.1
/usr/lib64/libmlx5.so.1.24.51.0
/usr/lib64/librdmacm.so.1
/usr/lib64/librdmacm.so.1.3.51.0
/usr/lib64/rsocket/librspreload.so
/usr/lib64/rsocket/librspreload.so.1
/usr/lib64/rsocket/librspreload.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/srp_daemon/start_on_all_ports

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rdma-core/133cf03905c2dc7d8a061e1d6e9ced3117b0120f
/usr/share/package-licenses/rdma-core/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/rdma-core/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/rdma-core/de66bb2ca6b007504c1844178dce4e48ef2adfff
/usr/share/package-licenses/rdma-core/df75be21090fc8aa92d1175f31b7891432da3d09
/usr/share/package-licenses/rdma-core/eaff686ba07863809da758bed796270f84c877ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cmtime.1
/usr/share/man/man1/ib_acme.1
/usr/share/man/man1/ibv_asyncwatch.1
/usr/share/man/man1/ibv_devices.1
/usr/share/man/man1/ibv_devinfo.1
/usr/share/man/man1/ibv_rc_pingpong.1
/usr/share/man/man1/ibv_srq_pingpong.1
/usr/share/man/man1/ibv_uc_pingpong.1
/usr/share/man/man1/ibv_ud_pingpong.1
/usr/share/man/man1/ibv_xsrq_pingpong.1
/usr/share/man/man1/mckey.1
/usr/share/man/man1/rcopy.1
/usr/share/man/man1/rdma_client.1
/usr/share/man/man1/rdma_server.1
/usr/share/man/man1/rdma_xclient.1
/usr/share/man/man1/rdma_xserver.1
/usr/share/man/man1/riostream.1
/usr/share/man/man1/rping.1
/usr/share/man/man1/rstream.1
/usr/share/man/man1/ucmatose.1
/usr/share/man/man1/udaddy.1
/usr/share/man/man1/udpong.1
/usr/share/man/man5/iwpmd.conf.5
/usr/share/man/man5/srp_daemon.service.5
/usr/share/man/man5/srp_daemon_port@.service.5
/usr/share/man/man7/efadv.7
/usr/share/man/man7/hnsdv.7
/usr/share/man/man7/ibacm.7
/usr/share/man/man7/ibacm_prov.7
/usr/share/man/man7/manadv.7
/usr/share/man/man7/mlx4dv.7
/usr/share/man/man7/mlx5dv.7
/usr/share/man/man7/rdma_cm.7
/usr/share/man/man7/rsocket.7
/usr/share/man/man7/rxe.7
/usr/share/man/man8/check_lft_balance.8
/usr/share/man/man8/dump_fts.8
/usr/share/man/man8/dump_lfts.8
/usr/share/man/man8/dump_mfts.8
/usr/share/man/man8/ibacm.8
/usr/share/man/man8/ibaddr.8
/usr/share/man/man8/ibcacheedit.8
/usr/share/man/man8/ibccconfig.8
/usr/share/man/man8/ibccquery.8
/usr/share/man/man8/ibfindnodesusing.8
/usr/share/man/man8/ibhosts.8
/usr/share/man/man8/ibidsverify.8
/usr/share/man/man8/iblinkinfo.8
/usr/share/man/man8/ibnetdiscover.8
/usr/share/man/man8/ibnodes.8
/usr/share/man/man8/ibping.8
/usr/share/man/man8/ibportstate.8
/usr/share/man/man8/ibqueryerrors.8
/usr/share/man/man8/ibroute.8
/usr/share/man/man8/ibrouters.8
/usr/share/man/man8/ibsrpdm.8
/usr/share/man/man8/ibstat.8
/usr/share/man/man8/ibstatus.8
/usr/share/man/man8/ibswitches.8
/usr/share/man/man8/ibsysstat.8
/usr/share/man/man8/ibtracert.8
/usr/share/man/man8/infiniband-diags.8
/usr/share/man/man8/iwpmd.8
/usr/share/man/man8/perfquery.8
/usr/share/man/man8/rdma-ndd.8
/usr/share/man/man8/saquery.8
/usr/share/man/man8/sminfo.8
/usr/share/man/man8/smpdump.8
/usr/share/man/man8/smpquery.8
/usr/share/man/man8/srp_daemon.8
/usr/share/man/man8/vendstat.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ibacm.service
/usr/lib/systemd/system/ibacm.socket
/usr/lib/systemd/system/iwpmd.service
/usr/lib/systemd/system/rdma-hw.target
/usr/lib/systemd/system/rdma-load-modules@.service
/usr/lib/systemd/system/rdma-ndd.service
/usr/lib/systemd/system/srp_daemon.service
/usr/lib/systemd/system/srp_daemon_port@.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbnxt_re-rdmav34.a
/usr/lib64/libcxgb4-rdmav34.a
/usr/lib64/libefa.a
/usr/lib64/liberdma-rdmav34.a
/usr/lib64/libhfi1verbs-rdmav34.a
/usr/lib64/libhns.a
/usr/lib64/libibmad.a
/usr/lib64/libibnetdisc.a
/usr/lib64/libibumad.a
/usr/lib64/libibverbs.a
/usr/lib64/libipathverbs-rdmav34.a
/usr/lib64/libirdma-rdmav34.a
/usr/lib64/libmana.a
/usr/lib64/libmlx4.a
/usr/lib64/libmlx5.a
/usr/lib64/libmthca-rdmav34.a
/usr/lib64/libocrdma-rdmav34.a
/usr/lib64/libqedr-rdmav34.a
/usr/lib64/librdmacm.a
/usr/lib64/librxe-rdmav34.a
/usr/lib64/libsiw-rdmav34.a
/usr/lib64/libvmw_pvrdma-rdmav34.a
