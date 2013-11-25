# Contributor: Mladen Milinkovic <maxrd2@smoothware.net>
# Maintainer: Mladen Milinkovic <maxrd2@smoothware.net>

pkgname=subtitlecomposer
pkgver=0.5.6
pkgrel=1
pkgdesc="A KDE subtitle editor"
arch=('i686' 'x86_64')
url="https://github.com/maxrd2/subtitlecomposer"
license=('GPL')
depends=('kdelibs' 'gettext')
makedepends=('cmake' 'automoc4' 'git')
conflicts=('subtitlecomposer-git')
optdepends=(
	'mplayer: for MPlayer backend'
	'mplayer2: for MPlayer backend'
	'gstreamer: for GStreamer backend'
	'xine-lib: for Xine backend'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/maxrd2/subtitlecomposer/archive/v${pkgver}.tar.gz")
sha256sums=('f55f3330e72a9a9f19f00674651d7d4c6cd7e19993a14d1deedfa6d34737cf0f')

build() {
	cd ${srcdir}/subtitlecomposer-${pkgver}
	cmake -DCMAKE_INSTALL_PREFIX=/usr
	make
}

package() {
	cd ${srcdir}/subtitlecomposer-${pkgver}
	make DESTDIR=${pkgdir} install
}
