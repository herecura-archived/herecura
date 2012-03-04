# Maintainer: garion < garion @ mailoo.org >

pkgname=mkclean
pkgver=0.8.6
pkgrel=2
pkgdesc="Clean up and optimize MKV files"
arch=('i686' 'x86_64')
url="http://www.matroska.org/downloads/$pkgname.html"
license=('BSD')
depends=('libebml' 'libmatroska')
source=("https://downloads.sourceforge.net/project/matroska/$pkgname/$pkgname-$pkgver.tar.bz2")

if [ "$CARCH" = "i686" ]; then
  _gcc_linux="gcc_linux"
elif [ "$CARCH" = "x86_64" ]; then
  _gcc_linux="gcc_linux_x64"
else
  return 1
fi

build() {
  cd $pkgname-$pkgver
  ./configure || return 1
  make -C $pkgname || return 1
}

package(){
  cd $pkgname-$pkgver
  install -Dm755 "release/$_gcc_linux/$pkgname"   "$pkgdir/usr/bin/"
  install -Dm755 "release/$_gcc_linux/mkcleanreg" "$pkgdir/usr/bin/"
  install -Dm755 "release/$_gcc_linux/mkWDclean"  "$pkgdir/usr/bin/"
}
sha256sums=('6e81a7522ef47ddfefb4ae1f5d9bee217190741b6660f5240dba85bc4faf4a44')
