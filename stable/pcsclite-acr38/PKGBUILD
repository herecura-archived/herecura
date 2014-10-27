# Contributor: Geuten Edouard <edouard@grima.be>
# Contributor: Thibaud de Borggraef <thibaud.deborggraef@telenet.be>

pkgname=pcsclite-acr38
pkgver=1.0.7.10
pkgrel=1
pkgdesc="PC/SC Drivers for ACR38 smart card reader"
arch=('i686' 'x86_64')
url="http://www.acs.com.hk/drivers-manual.php?driver=ACR38"
license=("LGPL")
depends=('pcsclite' 'libusb-compat')
source=('http://www.acs.com.hk/drivers/eng/ACR38U_driver_Lnx_1710_P.tar.gz')
md5sums=('386ad8025ce226433526f03ed910946d')

build() {
	cd ACR38_LINUX_100710_P
	./configure --prefix=/usr --sysconfdir=/etc
	make
}

package() {
	cd ACR38_LINUX_100710_P
	make DESTDIR="$pkgdir" usbdropdir="$pkgdir/usr/lib/pcsc/drivers" install
} 
