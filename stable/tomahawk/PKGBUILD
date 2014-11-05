# Maintainer: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>
# https://github.com/zizzfizzix/pkgbuilds

pkgname=tomahawk
pkgver=0.8.0
pkgrel=1
pkgdesc="A Music Player App written in C++/Qt"
arch=('i686' 'x86_64')
url="http://tomahawk-player.org/"
license=('GPL3')
depends=('phonon-qt4' 'taglib' 'boost' 'lucene++' 'libechonest2' 'jreen' 'qtweetlib' 'quazip' 'attica-qt4' 'qtwebkit' 'liblastfm' 'sparsehash' 'qtkeychain' 'websocketpp')
makedepends=('cmake')
provides=('tomahawk')
conflicts=('tomahawk-git')
source=("http://download.tomahawk-player.org/${pkgname}-${pkgver}.tar.bz2")

install=tomahawk.install

prepare() {
  [[ -e build ]] && rm -rf build
  mkdir build

  # shared lib fix/hack
  sed '/CMAKE_SHARED_LINKER_FLAGS/d' -i "$pkgname-$pkgver"/CMakeLists.txt
  sed '/CMAKE_SHARED_LINKER_FLAGS/d' -i "$pkgname-$pkgver"/src/libtomahawk/CMakeLists.txt
}

build() {
  cd build

  cmake -DBUILD_WITH_QT4=on \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_LIBEXECDIR=lib/${pkgname} \
        -DCMAKE_BUILD_TYPE=Release \
        ../${pkgname}-${pkgver}
  make
}

package() {
  cd build
  make DESTDIR=${pkgdir} install
}

sha256sums=('3ec840d7834b856c1a04575388935e613698db391e1096604048c8d1a50d55d9')
