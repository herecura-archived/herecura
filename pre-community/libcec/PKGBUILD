# $Id$
# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Philippe Cherel <philippe.cherel@mayenne.org>
# vim: ft=sh:

pkgname=libcec
pkgver=2.1.3
pkgrel=3
pkgdesc="Pulse-Eight's libcec for the Pulse-Eight USB-CEC adapter"
arch=('i686' 'x86_64')
url="http://libcec.pulse-eight.com/"
license=('GPL')
depends=('udev' 'lockdev')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Pulse-Eight/$pkgname/archive/$pkgname-$pkgver.tar.gz")
sha256sums=('2aa88451b528184b02077ee8c6cd10e2f89121a6a05b1b35b4b792b03108a9d1')

build() {
  cd "$pkgname-$pkgname-$pkgver"
  autoreconf -vif
  ./configure --prefix=/usr
  make
}

package() {
  cd "$pkgname-$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
