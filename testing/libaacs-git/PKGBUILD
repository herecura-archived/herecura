# Maintainer: Dirk Berg <dberg1981@googlemail.com>

pkgname=libaacs-git
pkgver=20130313
pkgrel=1
pkgdesc="Blu-Ray aacs library"
arch=('i686' 'x86_64')
depends=()
license=('LGPL')
url="http://www.videolan.org/developers/libaacs.html"
makedepends=('git' 'flex' 'byacc')
source=()
sha256sums=()
provides=('libaacs')
conflicts=('libaacs')

_gitroot="git://git.videolan.org/libaacs.git"
_gitname="libaacs"

build() {
    msg "Connecting to GIT server..."

    if [ -d ${srcdir}/$_gitname ] ; then
        cd $_gitname && git pull origin
        msg "The local files are updated."
    else
        git clone $_gitroot
    fi

    msg "GIT checkout done or server timeout"
    msg "Starting make..."

    cd ${srcdir}/libaacs
	sed -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' -i configure.ac
    ./bootstrap
    ./configure --prefix=/
    make
}

package() {
    cd ${srcdir}/libaacs
    make DESTDIR=${pkgdir}/usr install
}
