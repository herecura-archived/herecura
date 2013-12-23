pkgname=kdm-theme-caledonia
pkgver=1.3
pkgrel=1
pkgdesc="A minimalist and elegant kdm theme"
arch=('any')
url='http://sourceforge.net/projects/caledonia/'
license=('CCPL')
depends=('kdebase-workspace')
source=("$pkgname-$pkgver.tar.gz::http://downloads.sourceforge.net/project/caledonia/Caledonia%20KDM/Caledonia-KDM.tar.gz")
sha256sums=('cba3479e5c4720ee02aa4ef1647f1a5931c82e30a72578b35e6cc79b1e53320f')

package() {
  install -dm 755 "$pkgdir/usr/share/apps/kdm/themes/"
  cp -a "$srcdir/Caledonia-KDM" "$pkgdir/usr/share/apps/kdm/themes/"
}

# vim:set ft=sh:
