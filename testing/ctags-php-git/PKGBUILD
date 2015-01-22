# Maintainer: Alex "grevus" Lobtsov <alex@lobtsov.com>
pkgname=ctags-php-git
pkgver=20140428.4ebe089
pkgrel=1
pkgdesc="Generates an index file of language objects found in source files. Enhanced for php."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/b4n/ctags"

depends=('glibc')
makedepends=('git')

conflicts=('ctags')
provides=('ctags')

source=("$pkgname::git://github.com/b4n/ctags.git#branch=better-php-parser")

sha256sums=('SKIP')

pkgver() {
	cd "$pkgname"
	git log -1 --date=short --format="%cd.%h" | tr -d '-'
}

build() {
	cd "$pkgname"

	autoheader
	autoconf
	./configure --prefix=/usr \
		--disable-external-sort

	make
}

package() {
	cd "$pkgname"

	make prefix=${pkgdir}/usr install
}
