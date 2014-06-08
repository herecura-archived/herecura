# Maintainer: SpepS <dreamspepser at yahoo dot it>
# Contributor: Roman Kyrylych <roman@archlinux.org>
# Contributor: orelien <aurelien.foret@wanadoo.fr>

pkgname=httrack
pkgver=3.48.13
pkgrel=1
pkgdesc="An easy-to-use offline browser utility."
arch=('i686' 'x86_64')
url="http://www.httrack.com/"
license=('GPL')
depends=('bash' 'zlib')
options=('!libtool' '!makeflags')
install="$pkgname.install"
source=("http://download.httrack.com/$pkgname-$pkgver.tar.gz")

build() {
  cd "$pkgname-$pkgver"

  ./configure --prefix=/usr \
              --enable-static=no
  make
}

package() {
  cd "$pkgname-$pkgver"

  make DESTDIR="$pkgdir" install
}
sha256sums=('02c34571e974605b0a0398c1c65336bbe94142391d61a9be4234c2d19b09e947')
