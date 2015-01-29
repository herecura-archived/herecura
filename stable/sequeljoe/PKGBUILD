# Maintainer: Oliver Giles <web ohwg net>
pkgname=sequeljoe
pkgver=0.3
pkgrel=1
pkgdesc="SQL database administration tool"
arch=('i686' 'x86_64')
url="http://sequeljoe.ohwg.net"
license=('GPL3')
groups=()
depends=('qt5-base' 'libssh2' 'libnotify')
optdepends=(
   'libmariadbclients: MySQL/MariaDB support'
   'sqlite: sqlite support'
)
makedepends=('cmake')
options=('strip')
source=("https://github.com/ohwgiles/sequeljoe/archive/$pkgver.zip")

build() {
	cd "$srcdir/$pkgname-$pkgver"
	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release src
	make -j4
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}

sha256sums=('169b8560ab13d3e264285fc1e14ad4e3ab1af16069f3ab25251f5f11513bbbd5')
