# Maintainer: Jeff Meldrum <jeffmeld(AT)lightspeed(DOT)ca>

pkgname=nmapsi4
pkgver=0.3.2
pkgrel=1
pkgdesc="Qt-based Gui nmap interface."
arch=('i686' 'x86_64')
url="http://nmapsi.sourceforge.net/"
license=('GPL2')
conflicts=()
depends=('qt' 'qtwebkit' 'nmap')
makedepends=('cmake>=2.6')
source=("http://nmapsi4.googlecode.com/files/$pkgname-$pkgver.tar.bz2")

build() {
	cd $pkgname-$pkgver
	# Run cmake script
	cd tools
	./cmake_verbose_script.sh

	cd ../build
	# Change package location to /usr from /usr/local
	sed -i 's_/usr/local_/usr_' ./cmake_install.cmake

	make
}

package() {
	cd $pkgname-$pkgver/build
	make DESTDIR="$pkgdir" install
	chmod +x "$pkgdir/usr/bin"/*
}
sha256sums=('6bcb94b869c68f2b1ebba258c93af2fbcc6842c60e880dfb08f07de8f3b31759')
