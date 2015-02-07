# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=346.35
_extramodules=3.18-BEDE-external
pkgrel=4
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.18.6' 'linux-bede<3.19' 'linux-bede-headers>=3.18' 'linux-bede-headers<3.19' "nvidia-utils=$pkgver" "nvidia-libgl=$pkgver")
conflicts=('nvidia-96xx' 'nvidia-173xx')
replaces=('nvidia-bemm')
license=('custom')
install=nvidia.install
options=(!strip)

source=(
    "http://download.nvidia.com/XFree86/Linux-x86/$pkgver/NVIDIA-Linux-x86-$pkgver.run"
    "http://download.nvidia.com/XFree86/Linux-x86_64/$pkgver/NVIDIA-Linux-x86_64-$pkgver-no-compat32.run"
)

[[ "$CARCH" = "i686" ]] && _pkg="NVIDIA-Linux-x86-${pkgver}"
[[ "$CARCH" = "x86_64" ]] && _pkg="NVIDIA-Linux-x86_64-${pkgver}-no-compat32"

prepare() {
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    sh $_pkg.run --extract-only
    cd $_pkg
    # patch if needed
}

build() {
    _kernver="$(cat /usr/lib/modules/$_extramodules/version)"
    cd $_pkg/kernel
    make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package() {
    depends=('linux-bede>=3.18' 'linux-bede<3.19' "nvidia-utils=${pkgver}" "nvidia-libgl=$pkgver")

    install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
        "$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

    install -dm755 "$pkgdir/usr/lib/modprobe.d"
    echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
    echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

    # gzip all modules
    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}

sha256sums=('bba63c30c730ad7b8500a77c81cae58562b9f9b57cd576b61f37a2d8bc45df25'
            '7dae481224fddc711c2478e92ae0efd032acb0a002c85a44fa99ad9e54322afd')
