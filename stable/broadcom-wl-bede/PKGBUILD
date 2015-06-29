# Maintainer: graysky <graysky AT archlinux DOT org>
# Maintainer: Armin K. <krejzi at email dot com>
# Contributor: Austin ( doorknob60 [at] gmail [dot] com )
# Contributor: Gaetan Bisson <bisson@archlinux.org>

pkgname=broadcom-wl-bede
pkgver=6.30.223.248
pkgrel=20
_pkgdesc='Broadcom 802.11abgn hybrid Linux networking device driver for linux-bede'
_extramodules=4.1-BEDE-external
pkgdesc="${_pkgdesc}"
arch=('i686' 'x86_64')
url='http://www.broadcom.com/support/802.11/linux_sta.php'
license=('custom')
makedepends=('linux-bede>=4.1.1' 'linux-bede<4.2' 'linux-bede-headers>=4.1' 'linux-bede-headers<4.2')
source=('modprobe.d'
'license.patch'
'linux-recent.patch'
'gcc.patch')
source_i686=("http://www.broadcom.com/docs/linux_sta/hybrid-v35-nodebug-pcoem-${pkgver//./_}.tar.gz")
source_x86_64=("http://www.broadcom.com/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-${pkgver//./_}.tar.gz")
sha256sums=('b4aca51ac5ed20cb79057437be7baf3650563b7a9d5efc515f0b9b34fbb9dc32'
            '2f70be509aac743bec2cc3a19377be311a60a1c0e4a70ddd63ea89fae5df08ac'
            'ea2da813f890aa029d41b117f1b78d4379720c108101aef46aeb54df3c261f66'
            'b07ce80f2e079cce08c8ec006dda091f6f73f158c8a62df5bac2fbabb6989849')
sha256sums_i686=('b196543a429c22b2b8d75d0c1d9e6e7ff212c3d3e1f42cc6fd9e4858f01da1ad')
sha256sums_x86_64=('3d994cc6c05198f4b6f07a213ac1e9e45a45159899e6c4a7feca5e6c395c3022')

install=broadcom-wl-bede.install

prepare() {
	patch -p1 -i "$srcdir/linux-recent.patch"
	patch -p1 -i "$srcdir/license.patch"
	patch -p1 -i "$srcdir/gcc.patch"

	sed -e "/BRCM_WLAN_IFNAME/s:eth:wlan:" -i src/wl/sys/wl_linux.c
}


build() {
	_kernver="$(cat /usr/lib/modules/${_extramodules}/version)"
	make -C /usr/lib/modules/"${_kernver}"/build M=$(pwd)
}

package() {
	depends=('linux-bede>=4.1' 'linux-bede<4.2')

	install -Dm644 wl.ko "${pkgdir}/usr/lib/modules/${_extramodules}/wl.ko"

	# makepkg does not do this automatically for this pkg so do it here
	gzip -9 "${pkgdir}/usr/lib/modules/${_extramodules}/wl.ko"
	install -Dm644 lib/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm644 modprobe.d "${pkgdir}/usr/lib/modprobe.d/broadcom-wl_ck.conf"

    sed -i -e "s/EXTRAMODULES=.*/EXTRAMODULES='$_extramodules'/" "$startdir/broadcom-wl-bede.install"
}
