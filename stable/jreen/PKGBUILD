# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds

pkgname=jreen
pkgver=1.2.0
pkgrel=1
pkgdesc="Free and Opensource Jabber library, written in C++ using cross-platform framework Qt."
arch=('i686' 'x86_64')
url="http://qutim.org/jreen"
license=('GPL2')
depends=('libidn' 'qca-ossl' 'zlib' 'gsasl')
makedepends=('cmake')
provides=('jreen')
conflicts=('jreen-git')
source=("${pkgname}-${pkgver}.zip::http://github.com/euroelessar/${pkgname}/archive/v${pkgver}.zip"
	'jreenMacros.cmake.patch')

prepare() {
  if [[ -e "${pkgname}-${pkgver}-build" ]]; then
	  rm -rf "${pkgname}-${pkgver}-build"
  fi
  mkdir "${pkgname}-${pkgver}-build"

  cd "${pkgname}-${pkgver}/cmake"
  #patch -i "${srcdir}/jreenMacros.cmake.patch"
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
sha256sums=('e0f2e08309fa794aafe127508a59d255f4ecbe2f75ba53f2edc53e8cd179cb61'
            '52f719c34820747b577f2684fe4fa563b68df476b4b2e3d67886d3e74c4bf6db')
