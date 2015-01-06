# vim:set ft=sh:
# Maintainer: Dirk Berg <dberg1981@googlemail.com>

pkgname=libaacs-git
_gitname="libaacs"
pkgver=20150105.d5e655c
pkgrel=1
pkgdesc="Blu-Ray aacs library"
arch=('i686' 'x86_64')
depends=()
license=('LGPL')
url="http://www.videolan.org/developers/libaacs.html"
makedepends=('git' 'flex' 'byacc')
source=("$_gitname::git://git.videolan.org/libaacs.git")
sha256sums=('SKIP')
provides=('libaacs')
conflicts=('libaacs')

pkgver() {
	cd "$srcdir/$_gitname"
	git log -1 --date=short --format="%cd.%h" | tr -d '-'
}

build() {
    cd ${srcdir}/$_gitname
	sed -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' -i configure.ac
    ./bootstrap
    ./configure --prefix=/
    make
}

package() {
    cd ${srcdir}/$_gitname
    make DESTDIR=${pkgdir}/usr install
}
