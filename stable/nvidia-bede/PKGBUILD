# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=334.21
_extramodules=3.14-BEDE-external
pkgrel=6
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.14.1' 'linux-bede<3.15' 'linux-bede-headers>=3.14' 'linux-bede-headers<3.15' "nvidia-utils=$pkgver" "nvidia-libgl=$pkgver")
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
    sha256sums=('ece6ac1d66b0de53b6db0ae92f72112f734c9ec4b7f1ffb1ec508d32f700df39')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-$_arch-$pkgver-no-compat32"
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run")
    sha256sums=('55d1be4eda82b2a4c56925720f4f54d921647abcf9a715d8ccdc09e5f2351470')
fi

source+=('nvidia-linux-3.14.patch')
sha256sums+=('5f0fe6be7c610e61a7e3cd45b98581cd3285ceb8469a7b2e3629e7a95f641126')

prepare() {
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    sh $_pkg.run --extract-only
    cd $_pkg
    # patch if needed
    patch -p1 -i "${srcdir}"/nvidia-linux-3.14.patch
}

build() {
    _kernver="$(cat /usr/lib/modules/$_extramodules/version)"
    cd $_pkg/kernel
    make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package() {
    depends=('linux-bede>=3.14' 'linux-bede<3.15' "nvidia-utils=${pkgver}" "nvidia-libgl=$pkgver")

    install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
        "$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

    install -dm755 "$pkgdir/usr/lib/modprobe.d"
    echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
    echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

    # gzip all modules
    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}

