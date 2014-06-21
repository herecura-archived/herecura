pkgname=libgroove
pkgver=4.1.1
pkgrel=1
pkgdesc="Audio dispatching library. Generic sink-based interface. Provides decoding, encoding, resampling, and gain adjustment."
arch=('i686' 'x86_64')
url="https://github.com/andrewrk/libgroove"
license=('MIT')
depends=('sdl2' 'lame' 'bzip2' 'ffmpeg' 'chromaprint')
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

sha256sums=('a852936e5da65e1729bc85b20e2a6ace71c3813abd77dac44759b3db8659bea6')
