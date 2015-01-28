# Maintainer: ava1ar <mail(at)ava1ar(dot)info>

pkgname=chrome-pepper-flash
pkgdesc="Google Chrome's Pepper Flash plugin for ppapi compatible browsers (stable version)"
pkgver=16.0.0.296
pkgrel=1
_verbld=40.0.2214.93
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
	sed -e "s/flashver=.*/flashver=$pkgver/" -i "$startdir/chrome-pepper-flash.install"
	ar x "google-chrome-${_channel}_${_verbld}_${_arch}.deb"
	bsdtar -xf data.tar.lzma
}

package() {
	install -d "${pkgdir}/usr/lib/PepperFlash"
	install -m644 opt/google/chrome/PepperFlash/* "${pkgdir}/usr/lib/PepperFlash"
	install -Dm644 "${srcdir}/eula_text.html" "${pkgdir}/usr/share/licenses/${pkgname}/eula_text.html"
}

sha256sums=('8d2376f270bcaabcf7a4897efea3d2ed723b132c16a18b509ad5919c8993f07d'
            'c700d8e8e8df755485a0ffbfd89ae1f9e6ab14e1e828883a06da6c89b07d7000'
            '4242ecd421c56d47e56f6384be5621fe4e7b772c11036a72145d0e580a0f464c')
