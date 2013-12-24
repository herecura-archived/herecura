# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds

pkgname=tomahawk
pkgver=0.7.0
pkgrel=3
pkgdesc="A Music Player App written in C++/Qt"
arch=('i686' 'x86_64')
url="http://tomahawk-player.org/"
license=('GPL3')
depends=('phonon' 'taglib' 'boost' 'clucene' 'libechonest2' 'jreen' 'qtweetlib' 'quazip' 'attica' 'qtwebkit' 'liblastfm')
makedepends=('cmake')
provides=('tomahawk')
conflicts=('tomahawk-git')
source=("http://download.tomahawk-player.org/${pkgname}-${pkgver}.tar.bz2")
md5sums=('98b7f5bc43e017379f5cd3834f19e90d')

install=tomahawk.install

build() {
  if [[ -e ${srcdir}/${pkgname}-${pkgver}-build ]]; then
	  rm -rf ${srcdir}/${pkgname}-${pkgver}-build
  fi
  mkdir ${srcdir}/${pkgname}-${pkgver}-build
  cd ${srcdir}/${pkgname}-${pkgver}-build

  cmake -DBUILD_WITH_QT4=on \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_LIBEXECDIR=lib/${pkgname} \
        -DCMAKE_BUILD_TYPE=Release \
        ../${pkgname}-${pkgver}
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}-build
  make DESTDIR=${pkgdir} install
}
