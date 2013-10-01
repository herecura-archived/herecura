# vim:set ft=sh et:
# Maintainer : BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Thomas Baechler <thomas@archlinux.org>

_pkgname=nvidia
pkgname=$_pkgname-bede
pkgver=325.15
_extramodules=3.11-BEDE-external
pkgrel=13
pkgdesc="NVIDIA drivers for linux-bede"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('linux-bede>=3.11.3' 'linux-bede<3.12' 'linux-bede-headers>=3.11' 'linux-bede-headers<3.12' "nvidia-utils=$pkgver" "nvidia-libgl=$pkgver")
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
    sha256sums=('3d790e4bfed24641f7cc76879144ab5d52b12271012ba381b0d33aa1a2e08775')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-$_arch-$pkgver-no-compat32"
    source=("http://download.nvidia.com/XFree86/Linux-$_arch/$pkgver/$_pkg.run")
    sha256sums=('ee0dfa35c9b4da27a85684911a11236b82d63c171e0537624cce8ceccb7056e3')
fi

# 3.11 patch
source+=('kernel_v3.11.patch')
sha256sums+=('7a16034e0c526bb40acdf0740c917803d825f7d4682a9122e8afacfe80ff46d0')

build() {
    _kernver="$(cat /usr/lib/modules/$_extramodules/version)"
    cd "$srcdir"
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    sh $_pkg.run --extract-only
    (
        cd $_pkg
        patch -Np1 -i "$srcdir/kernel_v3.11.patch"
    )
    cd $_pkg/kernel
    make SYSSRC=/usr/lib/modules/$_kernver/build module
}

package() {
    depends=('linux-bede>=3.11' 'linux-bede<3.12' "nvidia-utils=${pkgver}" "nvidia-libgl=$pkgver")

    install -Dm644 "$srcdir/$_pkg/kernel/nvidia.ko" \
        "$pkgdir/usr/lib/modules/$_extramodules/$_pkgname/nvidia.ko"

    install -dm755 "$pkgdir/usr/lib/modprobe.d"
    echo "blacklist nouveau" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"
    echo "blacklist nvidiafb" >> "$pkgdir/usr/lib/modprobe.d/$pkgname.conf"

    # gzip all modules
    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='$_extramodules'/" "$startdir/nvidia.install"
}

