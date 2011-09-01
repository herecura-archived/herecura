# Contributor: ecst <elecst 4t gmail d0t com>

pkgname=byacc-noconflict
pkgver=20101229
pkgrel=1
pkgdesc="Non-conflicting version of byacc not providing bison/yacc"
arch=('i686' 'x86_64')
license=('custom')
url="ftp://invisible-island.net/byacc/"
depends=('glibc')
provides=('byacc')
source=(ftp://invisible-island.net/byacc/byacc-$pkgver.tgz)
md5sums=('e359702cda080c15f656a244aab132e5')

build() {
  cd $srcdir/byacc-$pkgver
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd $srcdir/byacc-$pkgver
  make DESTDIR=${pkgdir} install

#License
  sed -n "/is distributed/,/distributed freely/p" README > COPYING
  install -Dm644 COPYING ${pkgdir}/usr/share/licenses/$pkgname/COPYING

  cd $pkgdir/usr/bin
  mv yacc byacc
  cd $pkgdir/usr/share/man/man1
  mv yacc.1 byacc.1
}
