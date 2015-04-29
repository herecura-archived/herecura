# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-340xx-bede
pkgver=340.76
_extramodules=4.0-BEDE-external
pkgrel=10
pkgdesc="NVIDIA 340xx drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=4.0.1' 'linux-bede<4.1' 'linux-bede-headers>=4.0' 'linux-bede-headers<4.1' "nvidia-340xx-utils=$pkgver" "nvidia-340xx-libgl=$pkgver")
conflicts=('nvidia')
provides=('nvidia')
license=('custom')
install=nvidia.install
options=(!strip)

source=(
    "nv-drm.patch"
    "nvidia-4.0.patch"
)
source_i686=("http://download.nvidia.com/XFree86/Linux-x86/$pkgver/NVIDIA-Linux-x86-$pkgver.run")
source_x86_64=("http://download.nvidia.com/XFree86/Linux-x86_64/$pkgver/NVIDIA-Linux-x86_64-$pkgver-no-compat32.run")

sha256sums=('c9986c306f452614fcf23990c55ffe12bdc451bcbd65a5200269f90a722a3d35'
            '0b2594eec2ed869245041ead9a3cbe92e5b9b2461c3ede7406004ffae240d6e2')
sha256sums_i686=('9b29d93b49009caed84a8852825c3e7c6ebbbba8ec99b03ee5113108c8b036d0')
sha256sums_x86_64=('4c1ede2381cdd48139cdc4f3c657c5c347367160a6b1692bf09454969fb6d004')

[[ "$CARCH" = "i686" ]] && _pkg="NVIDIA-Linux-x86-${pkgver}"
[[ "$CARCH" = "x86_64" ]] && _pkg="NVIDIA-Linux-x86_64-${pkgver}-no-compat32"

prepare() {
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    sh $_pkg.run --extract-only
    cd $_pkg
    # patch if needed
    patch -p0 -i "$srcdir/nv-drm.patch"
    patch -p0 -i "$srcdir/nvidia-4.0.patch"
}

build() {
    _kernver="$(cat /usr/lib/modules/$_extramodules/version)"
    cd $_pkg/kernel
    make SYSSRC=/usr/lib/modules/$_kernver/build module

    if [[ "$CARCH" = "x86_64" ]]; then
        cd uvm
        make SYSSRC=/usr/lib/modules/"${_kernver}/build" module
    fi
}

package() {
    depends=('linux-bede>=4.0' 'linux-bede<4.1' "nvidia-340xx-utils=$pkgver" "nvidia-340xx-libgl=$pkgver")

    install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
        "$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

    if [[ "$CARCH" = "x86_64" ]]; then
        install -D -m644 "${srcdir}/${_pkg}/kernel/uvm/nvidia-uvm.ko" \
            "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-uvm.ko"
    fi

    install -dm755 "$pkgdir/usr/lib/modprobe.d"
    echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
    echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

    # gzip all modules
    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}

