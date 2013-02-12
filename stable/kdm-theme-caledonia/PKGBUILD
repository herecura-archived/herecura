pkgname=kdm-theme-caledonia
pkgver=1.0
pkgrel=1
pkgdesc="A minimalist and elegant kdm theme"
arch=('any')
url='http://sourceforge.net/projects/caledonia/'
license=('CCPL')
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20KDM/Caledonia-KDM.tar.gz")
sha256sums=('b74fb587be30a30dc61c9817733a29a20c6ab754932fa938b25a8a38cd0dce72')

package() {
  install -dm 755 "$pkgdir/usr/share/apps/kdm/themes/"
  cp -a "$srcdir/Caledonia-KDM" "$pkgdir/usr/share/apps/kdm/themes/"
}

# vim:set ft=sh:
