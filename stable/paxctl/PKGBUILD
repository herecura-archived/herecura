# Contributors:
#   sh0 <mee@sh0.org>
#   s1gma <s1gma@mindslicer.com>
#   henning mueller <henning@orgizm.net>

pkgname='paxctl'
pkgver='0.8'
pkgrel=1
pkgdesc='Manages various PaX related program header flags for Elf32, Elf64, binaries'
url='http://pax.grsecurity.net'
arch=('i686' 'x86_64')
license=('GPL')
depends=()
source=("http://pax.grsecurity.net/$pkgname-$pkgver.tar.gz")

prepare() {
  cd "${pkgname}-${pkgver}"
  sed -i 's:/sbin:/usr/bin:' Makefile
}

build() {
  cd "${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

sha256sums=('b5022768ed011a95bfe1770804349bf22a6973220997687d9a9ac58263aeef80')
