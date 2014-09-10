# Maintainer: ava1ar <mail(at)ava1ar(dot)info>

pkgname=chrome-pepper-flash
pkgdesc="Google Chrome's Pepper Flash plugin for ppapi compatible browsers (stable version)"
pkgver=15.0.0.152
pkgrel=1
_verbld=37.0.2062.120-1
_channel='stable'
arch=('i686' 'x86_64')
url="http://www.google.com/chrome"
license=('custom:chrome')
depends=('gcc-libs')
provides=("chromium-pepper-flash=${pkgver}" "chromium-pepper-flash-stable=${pkgver}")
replaces=("chromium-pepper-flash-stable")
optdepends=('pulseaudio-alsa: For PulseAudio users')
install=chrome-pepper-flash.install
source=(license.html::http://www.google.com/chrome/intl/en/eula_text.html)
sha1sums=('SKIP')
if [ "$CARCH" == x86_64 ]; then
	source+=(https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-${_channel}-${_verbld}.x86_64.rpm)
	sha1sums+=('74fdf78ca65f117987a43e71f896a8eb7605a6d2')
elif [ "$CARCH" == i686 ]; then
	source+=(https://dl.google.com/linux/chrome/rpm/stable/i386/google-chrome-${_channel}-${_verbld}.i386.rpm)
	sha1sums+=('e94917e2e47aa05c0c6764ff2e6a855324e64844')
fi

package() {
	install -d "${pkgdir}/usr/lib/PepperFlash"
	install -m644 opt/google/chrome/PepperFlash/* "${pkgdir}/usr/lib/PepperFlash"
	sed -i "s/flashver=.*/flashver=${pkgver}/" "${startdir}/chrome-pepper-flash.install"
	install -Dm644 "${srcdir}/license.html" "${pkgdir}/usr/share/licenses/${pkgname}/license.html"
}
