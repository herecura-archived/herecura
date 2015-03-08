# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=346.47
_extramodules=3.19-BEDE-external
pkgrel=3
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.19.1' 'linux-bede<3.20' 'linux-bede-headers>=3.19' 'linux-bede-headers<3.20' "nvidia-utils=$pkgver" "nvidia-libgl=$pkgver")
conflicts=('nvidia-96xx' 'nvidia-173xx')
replaces=('nvidia-bemm')
license=('custom')
install=nvidia.install
options=(!strip)

source_i686=("http://download.nvidia.com/XFree86/Linux-x86/$pkgver/NVIDIA-Linux-x86-$pkgver.run")
source_x86_64=("http://download.nvidia.com/XFree86/Linux-x86_64/$pkgver/NVIDIA-Linux-x86_64-$pkgver-no-compat32.run")

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

    if [[ "$CARCH" = "x86_64" ]]; then
        cd uvm
        make SYSSRC=/usr/lib/modules/"${_kernver}/build" module
    fi
}

package() {
    depends=('linux-bede>=3.19' 'linux-bede<3.20' "nvidia-utils=${pkgver}" "nvidia-libgl=$pkgver")

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

sha256sums_i686=('bb21527dfcd9855e3ae53ae5b56c29456902354c79f76d859d007068cdf76a6e')
sha256sums_x86_64=('d1b6672a9ddef2a01a527902b524dec232792cf9b61d3fa7bd0189488a961677')
