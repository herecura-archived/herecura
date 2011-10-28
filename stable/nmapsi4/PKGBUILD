# Maintainer: Jeff Meldrum <jeffmeld(AT)lightspeed(DOT)ca>

pkgname=nmapsi4
pkgver=0.2.1
pkgrel=1
pkgdesc="Qt-based Gui nmap interface."
arch=('i686' 'x86_64')
url="http://nmapsi.sourceforge.net/"
license=('GPL2')
conflicts=()
depends=('qt' 'nmap')
makedepends=('cmake>=2.6')
source=(http://nmapsi4.googlecode.com/files/${pkgname}-${pkgver}.tar.gz)
sha256sums=('4e7589b920473c0efa3aee3e818bd491ff271664fd1695c549b38dbcb5251c2e')

build() {
	cd ${pkgname}-${pkgver}
	# Run cmake script
	cd tools
	./cmake_verbose_script.sh

	cd ../build  
	# Change package location to /usr from /usr/local	
	sed -i 's_/usr/local_/usr_' ./cmake_install.cmake 

	make
}

package() {
	cd ${pkgname}-${pkgver}/build
	make DESTDIR=${pkgdir} install
	chmod +x ${pkgdir}/usr/bin/*
}
