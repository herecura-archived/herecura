# vim:set ft=sh:
# Maintainer: Dirk Berg <dberg1981@googlemail.com>

pkgname=libaacs-git
_gitname="libaacs"
pkgver=20131024.1e80832
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
	echo $(git log -1 --format="%ci" | sed 's/.*\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\).*/\1\2\3/').$(git rev-parse --short HEAD)
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
