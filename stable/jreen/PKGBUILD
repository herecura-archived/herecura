# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds

pkgname=jreen
_name=lib${pkgname}
pkgver=1.1.1
pkgrel=1
pkgdesc="Free and Opensource Jabber library, written in C++ using cross-platform framework Qt."
arch=('i686' 'x86_64')
url="http://qutim.org/jreen"
license=('GPL2')
depends=('libidn' 'qca-ossl' 'zlib')
makedepends=('cmake')
provides=('jreen')
conflicts=('jreen-git')
source=(http://qutim.org/dwnl/44/${_name}-${pkgver}.tar.bz2)
sha256sums=('607e3521b7fe8de54e7763e958efe05c5491f50f70a7d0811bdb8dea3515b5e2')

build() {
  if [[ -e ${srcdir}/${_name}-${pkgver}-build ]]; then
	  rm -rf ${srcdir}/${_name}-${pkgver}-build
  fi
  mkdir ${srcdir}/${_name}-${pkgver}-build
  cd ${srcdir}/${_name}-${pkgver}-build

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ../${_name}-${pkgver}
  make
}

package() {
  cd ${srcdir}/${_name}-${pkgver}-build
  make DESTDIR=${pkgdir} install
}
