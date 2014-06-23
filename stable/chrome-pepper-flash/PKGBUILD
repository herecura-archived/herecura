# Maintainer: ava1ar <mail(at)ava1ar(dot)info>

pkgname=chrome-pepper-flash
pkgdesc="Google Chrome's Pepper Flash plugin for ppapi compatible browsers (stable version)"
pkgver=14.0.0.125
pkgrel=5
_verbld=35.0.1916.153-1
_channel='stable'
arch=('i686' 'x86_64')
url="http://www.google.com/chrome"
license=('custom:chrome')
depends=('')
provides=("chromium-pepper-flash=${pkgver}" "chromium-pepper-flash-stable=${pkgver}")
replaces=("chromium-pepper-flash-stable")
optdepends=('pulseaudio-alsa: For PulseAudio users')
install=chrome-pepper-flash.install
source=(license.html::http://www.google.com/chrome/intl/en/eula_text.html)
sha1sums=('SKIP')
if [ "$CARCH" == x86_64 ]; then
        source+=(https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-${_channel}-${_verbld}.x86_64.rpm)
        sha1sums+=('0a39ec5296d90869ea211412c6197c57759f52d7')
elif [ "$CARCH" == i686 ]; then
        source+=(https://dl.google.com/linux/chrome/rpm/stable/i386/google-chrome-${_channel}-${_verbld}.i386.rpm)
        sha1sums+=('feed8f8d6bc5761d8ddf98435169668a64243bd6')
fi

package() {
	install -d "${pkgdir}/usr/lib/PepperFlash"
	install -m644 opt/google/chrome/PepperFlash/* "${pkgdir}/usr/lib/PepperFlash"
	sed -i "s/flashver=.*/flashver=${pkgver}/" "${startdir}/chrome-pepper-flash.install"
	install -Dm644 "${srcdir}/license.html" "${pkgdir}/usr/share/licenses/${pkgname}/license.html"
}
