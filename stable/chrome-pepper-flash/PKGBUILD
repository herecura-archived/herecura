# Maintainer: ava1ar <mail(at)ava1ar(dot)info>

pkgname=chrome-pepper-flash
pkgdesc="Google Chrome's Pepper Flash plugin for ppapi compatible browsers (stable version)"
pkgver=15.0.0.189
pkgrel=1
_verbld=38.0.2125.104
_channel='stable'
arch=('i686' 'x86_64')
url="http://www.google.com/chrome"
license=('custom:chrome')
depends=('gcc-libs')
provides=("chromium-pepper-flash=${pkgver}" "chromium-pepper-flash-stable=${pkgver}")
replaces=("chromium-pepper-flash-stable")
optdepends=('pulseaudio-alsa: For PulseAudio users')
install=chrome-pepper-flash.install

_arch=amd64
[[ $CARCH = i686 ]] && _arch=i386
source=(
	"google-chrome-${_channel}_${_verbld}_i386.deb::http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${_verbld}-1_i386.deb"
	"google-chrome-${_channel}_${_verbld}_amd64.deb::http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${_verbld}-1_amd64.deb"
	'http://www.google.com/chrome/intl/en/eula_text.html'
	
)
noextract=(
	"google-chrome-${_channel}_${_verbld}_i386.deb"
	"google-chrome-${_channel}_${_verbld}_amd64.deb"
)

prepare() {
	ar x "google-chrome-${_channel}_${_verbld}_${_arch}.deb"
	bsdtar -xf data.tar.lzma
}

package() {
	install -d "${pkgdir}/usr/lib/PepperFlash"
	install -m644 opt/google/chrome/PepperFlash/* "${pkgdir}/usr/lib/PepperFlash"
	sed -i "s/flashver=.*/flashver=${pkgver}/" "${startdir}/chrome-pepper-flash.install"
	install -Dm644 "${srcdir}/eula_text.html" "${pkgdir}/usr/share/licenses/${pkgname}/eula_text.html"
}

sha256sums=('be6cbc3ea91f1c47e88d5a54a4e2126492453072a60e322f28ae5d475634a45c'
            'a85e89a781405fcf4925a2691dd953fabae400c0600397c7c808933368aacb83'
            '4242ecd421c56d47e56f6384be5621fe4e7b772c11036a72145d0e580a0f464c')
