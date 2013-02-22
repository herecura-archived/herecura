# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=313.18
_extramodules=3.8-BEDE-external
pkgrel=5
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.8' 'linux-bede<3.9' 'linux-bede-headers>=3.8' 'linux-bede-headers<3.9' "nvidia-utils=$pkgver")
conflicts=('nvidia-96xx' 'nvidia-173xx')
replaces=('nvidia-bemm')
license=('custom')
install=nvidia.install
options=(!strip)

#source=("http://download.nvidia.com/XFree86/Linux-x86/$pkgver/NVIDIA-Linux-x86-$pkgver.run"
#"http://download.nvidia.com/XFree86/Linux-x86_64/$pkgver/NVIDIA-Linux-x86_64-$pkgver-no-compat32.run")

if [ "$CARCH" = "i686" ]; then
    _arch='x86'
    _pkg="NVIDIA-Linux-$_arch-$pkgver"
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run"
        '3.8_kernel.patch')
    sha256sums=('58e5e2191890ace94849444f5d2de4c2921dfe02cd97825d81a128754ff4488f'
        'e964fd876f21d7b0a4c91f308a384df97ac7d188707533b33520ba8d328af130')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-$_arch-$pkgver-no-compat32"
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run"
        '3.8_kernel.patch')
    sha256sums=('5e1611792e801cdf86ca5d9a8387839b56b533840891ff8ab5f8b1e4c8af408b'
        'e964fd876f21d7b0a4c91f308a384df97ac7d188707533b33520ba8d328af130')
fi

build() {
	_kernver="$(cat /usr/lib/modules/$_extramodules/version)"
	cd "$srcdir"
    [ -d "$_pkg" ] && rm -rf "$_pkg"
	sh $_pkg.run --extract-only
    cd $_pkg
    patch -Np0 -i $srcdir/3.8_kernel.patch
    cd kernel
 	make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package() {
	depends=('linux-bede>=3.8' 'linux-bede<3.9' "nvidia-utils=${pkgver}")

	install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
		"$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

	install -dm755 "$pkgdir/usr/lib/modprobe.d"
	echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
	echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

	# gzip all modules
	find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

	sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}

# vim:set ft=sh et:
