# Contributor: Austin ( doorknob60 [at] gmail [dot] com )
# Maintainer: Gaetan Bisson <bisson@archlinux.org>

pkgname=broadcom-wl-bede
pkgver=5.100.82.112
pkgrel=16
pkgdesc='Broadcom 802.11abgn hybrid Linux networking device driver'
url='http://www.broadcom.com/support/802.11/linux_sta.php'
arch=('i686' 'x86_64')
license=('custom')
depends=('linux-bede>=3.4' 'linux-bede<3.5')
makedepends=('linux-bede-headers>=3.4' 'linux-bede-headers<3.5')
install="$pkgname.install"

[[ $CARCH = x86_64 ]] && ARCH=x86_64 || ARCH=x86_32
source=("http://www.broadcom.com/docs/linux_sta/hybrid-portsrc_$ARCH-v${pkgver//./_}.tar.gz"
        'modprobe.d'
        'linux3.patch'
        'license.patch'
        'semaphore.patch'
		'bc_wl_abiupdate.patch'
		'linux34.patch')
sha1sums=('01aa32f9e85621253a3f15cf4361bb80d41da3e8'
          '89bf92286ede30dd85304c6c4e42e89cfdc0f60a'
          '3e18f905bbe5e8b99a53d6ecb3b80a919f3531f2'
          'ea7b67982ddc0f56fd3becb9914fd4458fe7d373'
          '105f8e1d48ebe1f25d53859e5ab9326a27435c66'
		  '229f41b7c371842bf9c1c81b03f34ee32fcb3310'
		  '3fcb657788cc69ab07e2775a34132c5792dc3a5e')
[[ $CARCH = x86_64 ]] && sha1sums[0]='5bd78c20324e6a4aa9f3fafdc6f0155e884d5131'

_extramodules=3.4-BEDE-external

build() {
	cd "$srcdir"

	patch -p1 -i linux3.patch
	patch -p1 -i license.patch
	patch -p1 -i semaphore.patch
	patch -p0 src/wl/sys/wl_linux.c < "$srcdir/bc_wl_abiupdate.patch"
	patch -Np0 -i linux34.patch

	_kernver="$(cat /usr/lib/modules/$_extramodules/version)"
	make -C "/usr/lib/modules/$_kernver/build" M=`pwd`
}

package() {
	cd "$srcdir"

	install -D -m 755 wl.ko "$pkgdir/usr/lib/modules/$_extramodules/broadcom-wl/wl.ko"
	gzip "$pkgdir/usr/lib/modules/$_extramodules/broadcom-wl/wl.ko"

	install -D -m 644 lib/LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -D -m 644 modprobe.d "$pkgdir/usr/lib/modprobe.d/broadcom-wl.conf"

	sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/$pkgname.install"
}
