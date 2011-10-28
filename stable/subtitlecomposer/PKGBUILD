# Contributor: Michal Malek <michalm@jabster.pl>
# Contributor: rraval

pkgname=subtitlecomposer
pkgver=0.5.3
pkgrel=4
pkgdesc="A KDE subtitle editor"
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/subcomposer"
license=('GPL')
depends=('kdelibs' 'gettext')
makedepends=('cmake' 'automoc4')
optdepends=("mplayer: for MPlayer backend")
source=(http://downloads.sourceforge.net/subcomposer/${pkgname}-${pkgver}.tar.bz2
        subtitlecomposer-build-fixes.patch
		subtitlecomposer-linkage.patch)
sha256sums=('87f3831b5ae09f4ffcefe586cd3b04b197784bf09652b02518b24a12fde2cad0'
            '5fdc27b3f2e7e8a897ad4f62122e84b628dbd51dfc3e1f70dfe4fa461a45ba94'
            '2af7bcf7b413a56b7abfa13df408fef7501989f694520ee609dea4b407f648b7')

# Many thanks for the linkage patch to the Gentoo guys.
# http://packages.gentoo.org/package/media-video/subtitlecomposer

build()
{
	cd ${pkgname}-${pkgver}

    # Patches
    patch -Np1 -i ${srcdir}/subtitlecomposer-build-fixes.patch
    patch -Np0 -i ${srcdir}/subtitlecomposer-linkage.patch

	sed -e '/ADD_SUBDIRECTORY( api )/s/^/# DISABLED/' \
		-i src/main/scripting/examples/CMakeLists.txt

	mkdir build
	cd build
	cmake .. -DCMAKE_INSTALL_PREFIX=/usr
	make

}

package() {
	cd ${pkgname}-${pkgver}/build
	make DESTDIR=${pkgdir} install
}
