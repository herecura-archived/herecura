# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds

pkgname=jreen
pkgver=1.1.1
pkgrel=2
pkgdesc="Free and Opensource Jabber library, written in C++ using cross-platform framework Qt."
arch=('i686' 'x86_64')
url="http://qutim.org/jreen"
license=('GPL2')
depends=('libidn' 'qca-ossl' 'zlib')
makedepends=('cmake')
provides=('jreen')
conflicts=('jreen-git')
source=("${pkgname}-${pkgver}.zip::http://github.com/euroelessar/${pkgname}/archive/v${pkgver}.zip"
	'jreenMacros.cmake.patch')
md5sums=('07e64faaae4be7cf2c99eac07f80fb8f'
         '397e75be409ea7e8bddff88b6f977f5f')

prepare() {
  if [[ -e "${pkgname}-${pkgver}-build" ]]; then
	  rm -rf "${pkgname}-${pkgver}-build"
  fi
  mkdir "${pkgname}-${pkgver}-build"

  cd "${pkgname}-${pkgver}/cmake"
  patch -i "${srcdir}/jreenMacros.cmake.patch"
}

build() {
  cd "${pkgname}-${pkgver}-build"

  cmake -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
        ../"${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}-build"
  make DESTDIR="${pkgdir}" install
}
