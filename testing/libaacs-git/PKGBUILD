# Maintainer: Dirk Berg <dberg1981@googlemail.com>

pkgname=libaacs-git
pkgver=20130101
pkgrel=1
pkgdesc="Blu-Ray aacs library"
arch=('i686' 'x86_64')
depends=()
license=('LGPL')
url="http://www.videolan.org/developers/libaacs.html"
makedepends=('git' 'flex' 'byacc')
source=('bison_2.6.patch')
sha256sums=('6ab15dd4b333bd40e965b9cae17052a95a5544065794ff8a26cb9fa71ad53320')
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
	patch -Np1 -i $srcdir/bison_2.6.patch
    ./bootstrap
    ./configure --prefix=/
    make
    make DESTDIR=${pkgdir}/usr install
}
