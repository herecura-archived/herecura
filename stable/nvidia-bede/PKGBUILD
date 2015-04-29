# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=349.16
_extramodules=4.0-BEDE-external
pkgrel=2
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=4.0' 'linux-bede<4.1' 'linux-bede-headers>=4.0' 'linux-bede-headers<4.1' "nvidia-utils=$pkgver" "nvidia-libgl=$pkgver")
conflicts=('nvidia')
provides=('nvidia')
license=('custom')
install=nvidia.install
options=(!strip)

source_i686=("http://download.nvidia.com/XFree86/Linux-x86/$pkgver/NVIDIA-Linux-x86-$pkgver.run")
source_x86_64=("http://download.nvidia.com/XFree86/Linux-x86_64/$pkgver/NVIDIA-Linux-x86_64-$pkgver-no-compat32.run")

sha256sums_i686=('35c8d00ece6a450e8e72aac2bff45e89ce40ffbe3278802e8a0b4ff65c793d11')
sha256sums_x86_64=('7d1222cd83f653ece0fb1a1141738db1d3b9930fc8a2edfdd8902bf07c5bed6d')

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
    depends=('linux-bede>=4.0' 'linux-bede<4.1' "nvidia-utils=${pkgver}" "nvidia-libgl=$pkgver")

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

