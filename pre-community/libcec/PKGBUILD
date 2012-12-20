# $Id: PKGBUILD 76478 2012-09-18 20:05:12Z idevolder $
# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Philippe Cherel <philippe.cherel@mayenne.org>

pkgname=libcec
pkgver=2.0.5
pkgrel=1
pkgdesc="Pulse-Eight's libcec for the Pulse-Eight USB-CEC adapter"
arch=('i686' 'x86_64')
url="https://github.com/Pulse-Eight/libcec"
license=('GPL')
depends=('udev' 'lockdev')
source=("$pkgname-$pkgver-repack.tar.gz::https://github.com/Pulse-Eight/libcec/tarball/$pkgname-$pkgver-repack")
_srcfolder=Pulse-Eight-libcec-d4a56bb
sha256sums=('ff876e793ad962d63d20e36f88a22965cb2f02ac793ac4297fcb76d8234b66cd')
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
