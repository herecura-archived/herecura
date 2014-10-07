pkgname=libgroove
pkgver=4.2.1
pkgrel=1
pkgdesc="Audio dispatching library. Generic sink-based interface. Provides decoding, encoding, resampling, and gain adjustment."
arch=('i686' 'x86_64')
url="https://github.com/andrewrk/libgroove"
license=('MIT')
depends=('sdl2' 'bzip2' 'ffmpeg' 'chromaprint' 'libebur128')
makedepends=('cmake' 'yasm')
conflicts=('libgroove-git')
options=('strip' 'ccache')
source=("https://github.com/andrewrk/libgroove/archive/$pkgver.tar.gz")

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	mkdir build
}

build() {
	cd "$srcdir/$pkgname-$pkgver/build"
	cmake ../ \
		-DCMAKE_BUILD_TYPE=Release \
    	-DCMAKE_INSTALL_PREFIX=/usr
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver/build"
	make DESTDIR="$pkgdir/" install
}

sha256sums=('82ba73ff44a3359f10899a11522521bdc9256b8bfad082a3fac49915e9f4d70f')
