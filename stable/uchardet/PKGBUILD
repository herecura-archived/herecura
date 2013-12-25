# Maintainer: Blake Imsland <blake@retroco.de>

pkgname=uchardet
pkgver=0.0.1
pkgrel=1
pkgdesc="An encoding detector library"
arch=('i686' 'x86_64')
url="http://code.google.com/p/uchardet/"
license=('MPL')
makedepends=('cmake')
source=("http://uchardet.googlecode.com/files/$pkgname-$pkgver.tar.gz")
sha256sums=('e238c212350e07ebbe1961f8f128faaa40f71b70d37b63ffa2fe12c664269ee6')

build() {
  cd "$srcdir/$pkgname-$pkgver"
	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
  make
}

check() {
  cd "$srcdir/$pkgname-$pkgver"
  #make -k check
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}
