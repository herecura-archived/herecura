# Maintainer: SJ_UnderWater
# Based on netatalk package :
# Maintainer: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.1.3
pkgrel=1
pkgdesc='A kernel-level implementation of AFP services'
arch=('i686' 'x86_64')
url='http://netatalk.sourceforge.net'
license=('GPL')
depends=('avahi>=0.6' 'libldap' 'libgcrypt>=1.2.3' 'libevent' 'python' 'dbus-glib')
replaces=('netatalk-git' 'netatalk2')
backup=('etc/afp.conf'
	'etc/extmap.conf')
options=('!libtool')
install=$pkgname.install
changelog=$pkgname.changelog
source=("http://downloads.sourceforge.net/project/$pkgname/$pkgname/$pkgver/$pkgname-$pkgver.tar.bz2")


build() {
	cd $pkgname-$pkgver
	msg2 'Configuring...'
	CFLAGS="-Wno-unused-result -O2" ./configure --prefix=/usr --localstatedir=/var/state --sysconfdir=/etc --sbindir=/usr/bin --with-init-style=systemd \
		--with-cracklib --with-cnid-cdb-backend --enable-pgp-uam --with-libevent=no
	sed -i -e s/-Ino// -e s/-Lno// etc/netatalk/Makefile
	msg2 'Making...'
	make
}

package() {
	cd $pkgname-$pkgver
	msg2 'Building...'
	make DESTDIR="$pkgdir" install
}

sha256sums=('e19d289400d7c9600653e2e6155506c00bbd4f5b6fe45f2e53b1843fe15f6b37')
