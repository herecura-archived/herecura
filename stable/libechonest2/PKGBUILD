# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds
# Contributor: Rick W. Chen <stuffcorpse@archlinux.us>

_pkgname=libechonest
pkgname=${_pkgname}2
pkgver=2.3.0
pkgrel=1
pkgdesc="C++ library for interfacing with Echo Nest"
arch=('i686' 'x86_64')
url="https://projects.kde.org/projects/playground/libs/libechonest"
license=('GPL')
depends=('qjson')
makedepends=('cmake' 'pkg-config')
provides=('libechonest')
conflicts=('libechonest-git' 'libechonest')
source=("http://files.lfranchi.com/${_pkgname}-${pkgver}.tar.bz2")

build() {
  cd ${srcdir}/${_pkgname}-${pkgver}

  if [[ -e ${srcdir}/${_pkgname}-${pkgver}-build ]]; then
	  rm -rf ${srcdir}/${_pkgname}-${pkgver}-build
  fi
  mkdir ${srcdir}/${_pkgname}-${pkgver}-build
  cd ${srcdir}/${_pkgname}-${pkgver}-build

  cmake -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
		-DECHONEST_BUILD_TESTS=off \
        ../${_pkgname}-${pkgver}
  make
}

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}-build
  make DESTDIR=${pkgdir} install
}

sha256sums=('79983ba72fbf9b112ebfb329b96b60eddf25d719ebe34eb70de01aa106ae2b44')
