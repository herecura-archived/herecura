# vim:set ts=2 sw=2 et:
# Maintainer: Davorin Učakar <davorin.ucakar@gmail.com>

pkgname=libsquish
pkgver=1.11
pkgrel=2
pkgdesc="DXT compression library"
arch=('i686' 'x86_64')
url="http://code.google.com/p/libsquish"
license=('MIT')
options=(staticlibs)
source=(http://libsquish.googlecode.com/files/squish-$pkgver.zip
        gcc440.patch
        config
        LICENSE)

prepare() {
  cd "$srcdir/squish-$pkgver"
  cp $srcdir/config .

  sed -e "s/\\(INSTALL_DIR\\).*/\\1 ?= ${pkgdir//\//\\/}\/usr/" -i config

  patch -Np0 -i $srcdir/gcc440.patch
}

build() {
  cd "$srcdir/squish-$pkgver"

  make
}

package() {
  cd "$srcdir/squish-$pkgver"

  install -dm755 "$pkgdir/usr"/{include,lib}

  make DESTDIR="$pkgdir" install

  install -Dm 644 $srcdir/LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}

sha256sums=('6e13120e2ec5fa34a116cafc23e48585ca7e963870b39bcd0bbe7df30aafa6a4'
            'c49fa616dcb1aa8eee523c20b70dd442358e051202091294686345daeb1d7352'
            'a06dd949e78371d5a471cd6cf1a4e3dab8b4fbc505b5cd35da33f0ae46d187b2'
            'ed13029728a637f599833a68be22f3cc356a7f13be8d79284b2c415e172efd75')
