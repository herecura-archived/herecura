# Maintainer: SJ_UnderWater
# Based on netatalk package :
# Maintainer: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.1.2
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

sha256sums=('040b6e9add6ad9f2a0a9a58f5f1381ee5e6b9a60e7610f6722747c834f1de990')
