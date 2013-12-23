pkgname=plasma-theme-caledonia
pkgver=1.5
pkgrel=1
pkgdesc="Elegant and minimalistic dark theme for plasma"
arch=('any')
license=('CCPL')
url='http://sourceforge.net/projects/caledonia/'
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20(Plasma-KDE%20Theme)/Caledonia.tar.gz")
sha256sums=('00a27c381d7f59625dc59112e4f76edac0dc53d44c2da9ee861743e4e8b63ab2')

package()
{
	install -dm 755 "$pkgdir/usr/share/apps/desktoptheme"
	cp -a "$srcdir/Caledonia" "$pkgdir/usr/share/apps/desktoptheme/"
	chmod u=rwX,og=rX -R "$pkgdir/usr/share/apps/desktoptheme/"
}

# vim:set ft=sh:
