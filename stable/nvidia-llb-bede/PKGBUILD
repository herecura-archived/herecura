# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Thomas Baechler <thomas@archlinux.org>
# Contributor: James Rayner <iphitus@gmail.com>
pkgname='nvidia-llb-bede'
pkgver=295.59
pkgrel=6
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
license=('custom')
options=('!strip')

makedepends=('linux-bede>=3.5' 'linux-bede<3.6' 'linux-bede-headers>=3.5' 'linux-bede-headers<3.6' "nvidia-llb-utils=${pkgver}")

_extramodules=3.5-BEDE-external

if [ "$CARCH" = "i686" ]; then
    _arch='x86'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}"
    source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
	md5sums=('bef732dfcf5cb079c06c1e8672d8d5dd')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
    source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
    md5sums=('864d5dd1a29cb303bd355707413e2b98')
fi

build() {
    cd "${srcdir}"
    sh "${_pkg}.run" --extract-only

	_kernver="$(cat /usr/lib/modules/$_extramodules/version)"
	cd $_pkg/kernel
	sed -e '/CFLAGS="$CFLAGS/s:-I$SOURCES/arch/x86/include:& -I$OUTPUT/arch/x86/include/generated:' -i conftest.sh
 	make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package_nvidia-llb-bede() {
	pkgdesc="NVIDIA drivers for linux-bede Long Lived Branch"
	depends=('linux-bede>=3.5' 'linux-bede<3.6' "nvidia-llb-utils=${pkgver}")
	conflicts=('nvidia-96xx' 'nvidia-173xx')
	provides=('nvidia')
	install=nvidia.install

	install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
		"$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

	install -dm755 "$pkgdir/usr/lib/modprobe.d"
	echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
	echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

	# gzip all modules
	find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

	sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}
