# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=310.14
_extramodules=3.6-BEDE-external
pkgrel=2
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.6' 'linux-bede<3.7' 'linux-bede-headers>=3.6' 'linux-bede-headers<3.7' "nvidia-utils=$pkgver")
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
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run")
    sha256sums=('c3616a40d2e13247939758bb648cf10a7d0fd00159a448c132194293039a7bcc')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-$_arch-$pkgver-no-compat32"
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run")
    sha256sums=('387341d9d7ddc8235594732f51fed1b39f73f62571038aff9a9db1c040b32e87')
fi

build() {
	_kernver="$(cat /usr/lib/modules/$_extramodules/version)"
	cd "$srcdir"
	sh $_pkg.run --extract-only
	cd $_pkg/kernel
	sed -e '/CFLAGS="$CFLAGS/s:-I$SOURCES/arch/x86/include:& -I$OUTPUT/arch/x86/include/generated:' -i conftest.sh
 	make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package() {
	depends=('linux-bede>=3.6' 'linux-bede<3.7' "nvidia-utils=${pkgver}")

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
