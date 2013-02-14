pkgname=plasma-theme-caledonia
pkgver=1.3
pkgrel=2
pkgdesc="Elegant and minimalistic dark theme for plasma"
arch=('any')
license=('CCPL')
url='http://sourceforge.net/projects/caledonia/'
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20(Plasma-KDE%20Theme)/Caledonia.tar.gz")
sha256sums=('f1fed242aefeebc62c815f435467d1b0f527014f6228237c4c97b9039e791bb3')

package()
{
	install -dm 755 "$pkgdir/usr/share/apps/desktoptheme"
	cp -a "$srcdir/Caledonia" "$pkgdir/usr/share/apps/desktoptheme/"
	chmod u=rwX,og=rX -R "$pkgdir/usr/share/apps/desktoptheme/"
}

# vim:set ft=sh:
