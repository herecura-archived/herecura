# $Id: PKGBUILD 76478 2012-09-18 20:05:12Z idevolder $
# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Philippe Cherel <philippe.cherel@mayenne.org>

pkgname=libcec
pkgver=2.0.2
pkgrel=1
pkgdesc="Pulse-Eight's libcec for the Pulse-Eight USB-CEC adapter"
arch=('i686' 'x86_64')
url="https://github.com/Pulse-Eight/libcec"
license=('GPL')
depends=('udev' 'lockdev')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Pulse-Eight/libcec/tarball/$pkgname-$pkgver")
_srcfolder=Pulse-Eight-libcec-a9ac151
sha256sums=('a61d1b550caa5a9b744df67a002f35a06486e373f79a167cedbc8583fa9c003c')
options=(!libtool)

build() {
  mv "$_srcfolder" "$pkgname-$pkgver"

  cd "$pkgname-$pkgver"
  sed 's/^LIBS_LIBCEC="$LIBS".*/LIBS_LIBCEC="$LIBS -fPIC"/' -i configure.ac
  autoreconf -vif
  LDFLAGS="$LDFLAGS -fPIC" ./configure --prefix=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
