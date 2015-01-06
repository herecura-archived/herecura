# Maintainer: Christian Neukirchen <chneukirchen@gmail.com>
# Maintainer of byacc: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: ecst <elecst 4t gmail d0t com>
# Contributor: Abel Stern <abel.stern AT gmail.com>
# Contributor: Anton Bazhenov <anton.bazhenov at gmail>

pkgname=byacc-noconflict
_pkgname=byacc
pkgver=20141128
pkgrel=1
pkgdesc="Non-conflicting version of byacc not providing bison/yacc"
arch=('i686' 'x86_64')
url="http://invisible-island.net/byacc/"
license=('custom')
depends=('glibc')
provides=('byacc')
source=(ftp://invisible-island.net/$_pkgname/$_pkgname-$pkgver.tgz
		ftp://invisible-island.net/$_pkgname/$_pkgname-$pkgver.tgz.asc)
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB')

build() {
  cd ${srcdir}/$_pkgname-$pkgver

  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd ${srcdir}/$_pkgname-$pkgver
  make DESTDIR=${pkgdir} install

  # License
  sed -n "/is distributed/,/distributed freely/p" README > COPYING
  install -Dm644 COPYING ${pkgdir}/usr/share/licenses/$pkgname/COPYING

  # Rename
  cd ${pkgdir}/usr/bin
  mv yacc byacc
  cd ${pkgdir}/usr/share/man/man1
  mv yacc.1 byacc.1
}

sha256sums=('f517fc21f08c1a1f010177357df58fc64eb1131011e5dcd48c19fe44c47198d0'
            'SKIP')
