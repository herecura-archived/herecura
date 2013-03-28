# Contributor: Diogo Leal <diogo@diogoleal.com>
# Contributor: Jan Fader <jan.fader@web.de>
# Contributor: xjpvictor Huang <ke [AT] xjpvictor [DOT] info>
pkgname=openswan
pkgver=2.6.38
pkgrel=3
pkgdesc="Open Source implementation of IPsec for the Linux operating system"
url="http://www.openswan.org"
license=('GPL' 'custom')
arch=('i686' 'x86_64')
depends=('iproute2>=2.6.8' 'gmp' 'perl')
makedepends=('flex' 'bison')
conflicts=('ipsec-tools' 'openswan')
provides=('openswan')
backup=(etc/ipsec.conf \
        etc/ipsec.d/policies/{block,clear,clear-or-private,private,private-or-clear})
source=(http://download.openswan.org/openswan/openswan-$pkgver.tar.gz
        openswan
        openswan.service
        ics.patch)
md5sums=('13073eb5314b83a31be88e4117e8bbcd'
         '543d84162761b9cc9ec319e938c4dd2a'
         'd8b465c10838c72e31329d65011002b6'
         'bef9e5d136103759f5d6cb5c1254c8c2')

build() {
  cd $srcdir/openswan-$pkgver
  patch -p1 -i $srcdir/ics.patch

  # Change install paths to Arch defaults
  sed -i 's|/usr/local|/usr|;s|libexec/ipsec|lib/openswan|' Makefile.inc

  make USE_XAUTH=true USE_OBJDIR=true programs
}

package() {
  cd $srcdir/openswan-$pkgver
  make DESTDIR=$pkgdir install

  # Create /etc/rc.d for init script, and license directory
  mkdir -p $pkgdir/{etc/rc.d,usr/share/licenses/openswan}

  # Change permissions in /var
  chmod 755 $pkgdir/var/run/pluto

  # Copy License
  cp LICENSE $pkgdir/usr/share/licenses/openswan

  # Install init script
  install -Dm755 ../openswan $pkgdir/etc/rc.d/openswan
  install -Dm644 ../openswan.service $pkgdir/usr/lib/systemd/system/openswan.service
  mkdir $pkgdir/usr/lib/systemd/scripts/
  mv $pkgdir/etc/rc.d/init.d/ipsec $pkgdir/usr/lib/systemd/scripts/ipsec
  rm -rf $pkgdir/etc/rc.d/init.d
  # fix manpages
  mv $pkgdir/usr/man $pkgdir/usr/share/
}
