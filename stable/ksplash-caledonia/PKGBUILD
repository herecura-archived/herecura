pkgname=ksplash-caledonia
pkgver=1.0
pkgrel=1
pkgdesc="Simple and lightweight splash screen for KDE"
arch=('any')
url='http://sourceforge.net/projects/caledonia/'
license=('CCPL')
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20KSplash/Caledonia-KSplash.tar.gz")
sha256sums=('435084ec25378d0506c40921a4af79828ea059b2dda0baa2cf0f1f53f81917c6')

package() {
	install -dm755 "$pkgdir/usr/share/apps/ksplash/Themes/"
	cp -a "$srcdir/Caledonia-KSplash" "$pkgdir/usr/share/apps/ksplash/Themes/"
}

# vim:set ft=sh:
