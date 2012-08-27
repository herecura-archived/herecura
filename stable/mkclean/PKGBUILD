# Maintainer: garion < garion @ mailoo.org >

pkgname=mkclean
pkgver=0.8.7
pkgrel=1
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
	./configure
	# fixing generated makefiles
	sed -i -e 's|^\(LFLAGS.*+=.*\$(LIBS)\)|\1 \$(LDFLAGS)|g' \
		-e 's|^\(STRIP.*=\)|\1 echo|g' $(find -name "*.mak")
	make -C $pkgname
}

package(){
	cd $pkgname-$pkgver
	install -Dm755 "release/$_gcc_linux/$pkgname"   "$pkgdir/usr/bin/$pkgname"
	install -Dm755 "release/$_gcc_linux/mkcleanreg" "$pkgdir/usr/bin/mkcleanreg"
	install -Dm755 "release/$_gcc_linux/mkWDclean"  "$pkgdir/usr/bin/mkWDclean"
}
sha256sums=('88713065a172d1ab7fd34c8854a42f6bf8d0e794957265340328a2f692ad46d9')
