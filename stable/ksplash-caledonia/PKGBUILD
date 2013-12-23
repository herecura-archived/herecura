pkgname=ksplash-caledonia
pkgver=1.3
pkgrel=1
pkgdesc="Simple and lightweight splash screen for KDE"
arch=('any')
url='http://sourceforge.net/projects/caledonia/'
license=('CCPL')
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20KSplash/Caledonia-KSplash.tar.gz")
sha256sums=('abfcfba96cf22ce3df75cf73d94f4aee09e953b52c24e1536ee6aaf35c7dc8ab')

package() {
	install -dm755 "$pkgdir/usr/share/apps/ksplash/Themes/"
	cp -a "$srcdir/Caledonia-KSplash" "$pkgdir/usr/share/apps/ksplash/Themes/"
}

# vim:set ft=sh:
