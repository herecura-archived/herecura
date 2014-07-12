# Maintainer: SpepS <dreamspepser at yahoo dot it>
# Contributor: Roman Kyrylych <roman@archlinux.org>
# Contributor: orelien <aurelien.foret@wanadoo.fr>

pkgname=httrack
pkgver=3.48.17
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
sha256sums=('7627fedefdb7d9e33112fa621aed08f2c13944311bbae716e989c388cfd4080f')
