# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Maintainer: Cedric Girard <girard.cedric@gmail.com>

pkgname=libplatform
pkgver=1.0.9
pkgrel=1
pkgdesc="Platform support library used by libCEC and binary add-ons for Kodi"
arch=('i686' 'x86_64')
url="https://github.com/Pulse-Eight/platform"
license=('GPL')
provides=('libplatform')
conflicts=('libplatform')
makedepends=('cmake')
depends=('gcc-libs')
source=(https://github.com/Pulse-Eight/platform/archive/${pkgver}.tar.gz)
sha256sums=('276dec2b8653fcf9bf636ac929bb014cc0963ccacd67179705d39301a9533b1e')

build() {
  cd "$srcdir"/platform-${pkgver}
  cmake . \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=1 \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCMAKE_INSTALL_LIBDIR_NOARCH=/usr/lib
  make
}

package() {
  cd "$srcdir"/platform-${pkgver}
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:
