# $Id$
# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Philippe Cherel <philippe.cherel@mayenne.org>
# vim: ft=sh:

pkgname=libcec
pkgver=2.1.3
pkgrel=4
pkgdesc="Pulse-Eight's libcec for the Pulse-Eight USB-CEC adapter"
arch=('i686' 'x86_64')
url="http://libcec.pulse-eight.com/"
license=('GPL')
depends=('udev' 'lockdev')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Pulse-Eight/$pkgname/archive/$pkgname-$pkgver.tar.gz")
sha256sums=('7afc162899c1b67000713e7719c6f89cd33f27f03a03c5bd5f281f8e6782989e')

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
