# $Id$
#Maintainer: Ionut Biru <ibiru@archlinux.org>

pkgbase=virtualbox-modules-bede
pkgname=('virtualbox-modules-bede-host' 'virtualbox-modules-bede-guest')
pkgver=4.1.14
pkgrel=1
arch=('i686' 'x86_64')
url='http://virtualbox.org'
license=('GPL')
makedepends=('libstdc++5' 'bin86' 'dev86' 'iasl' 'libxslt' 'libxml2' 'libpng' 'libidl2' 'xalan-c' 'sdl' 'linux-bede>=3.3' 'linux-bede<3.4' 'linux-bede-headers>=3.3' 'linux-bede-headers<3.4')
[[ $CARCH == "x86_64" ]] && makedepends=("${makedepends[@]}" 'gcc-multilib' 'lib32-glibc')
source=(
	"http://download.virtualbox.org/virtualbox/${pkgver}/VirtualBox-${pkgver}.tar.bz2"
	'LocalConfig.kmk'
	'60-vboxguest.rules'
)
md5sums=(
	'f8baa04e6d589bc6b1fb4e7079fbe414'
	'4c88bd122677a35f68abd76eb01b378b'
	'ed1341881437455d9735875ddf455fbe'
)

_extramodules=3.3-BEDE-external

build() {
	_kernver="$(cat /lib/modules/${_extramodules}/version)"

	export KERN_DIR=/lib/modules/${_kernver}/build
	export KERN_INCL=/usr/src/linux-${_kernver}/include/

    cd "$srcdir/VirtualBox-${pkgver}"

    cp "$srcdir/LocalConfig.kmk" .

    ./configure \
        --with-linux=/usr/src/linux-${_kernver} \
        --disable-java \
        --disable-docs \
        --disable-xpcom \
        --disable-python \
        --disable-sdl-ttf \
        --disable-alsa \
        --disable-pulse \
        --disable-dbus  \
        --disable-opengl \
        --build-headless \
        --nofatal
    source ./env.sh
    kmk all

    make -C "$srcdir/VirtualBox-${pkgver}/out/linux.$BUILD_PLATFORM_ARCH/release/bin/src"
    make -C "$srcdir/VirtualBox-${pkgver}/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions/src"
}

package_virtualbox-modules-bede-host(){
	pkgdesc="Kernel modules for VirtualBox (linux-bede)"
    license=('GPL')
    install=virtualbox-modules-bede-host.install
    depends=('linux-bede>=3.3' 'linux-bede<3.4')
	provides=("virtualbox-modules=${pkgver}")

    source "$srcdir/VirtualBox-${pkgver}/env.sh"


    cd "$srcdir/VirtualBox-${pkgver}/out/linux.$BUILD_PLATFORM_ARCH/release/bin/src"

    for module in vboxdrv.ko vboxnetadp.ko vboxnetflt.ko vboxpci.ko; do
        install -D -m644 ${module} \
            "$pkgdir/lib/modules/${_extramodules}/vbox/${module}"
    done

    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "$startdir/virtualbox-modules-bede-host.install"
}

package_virtualbox-modules-bede-guest(){
	pkgdesc="Additions only for Arch Linux guests (kernel modules) (linux-bede)"
    license=('GPL')
    install=virtualbox-modules-bede-guest.install
    depends=('linux-bede>=3.3' 'linux-bede<3.4')
	provides=("virtualbox-archlinux-modules=${pkgver}")

    source "$srcdir/VirtualBox-${pkgver}/env.sh"

    cd "$srcdir/VirtualBox-${pkgver}/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions/src"

    for module in vboxguest.ko vboxsf.ko vboxvideo.ko; do
        install -D -m644 ${module} \
            "$pkgdir/lib/modules/${_extramodules}/vbox/${module}"
    done

    install -D -m 0644 "$srcdir/60-vboxguest.rules" \
        "$pkgdir/usr/lib/udev/rules.d/60-vboxguest-bede.rules"

    find "$pkgdir" -name '*.ko' -exec gzip -9 {} \;

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "$startdir/virtualbox-modules-bede-guest.install"
}
