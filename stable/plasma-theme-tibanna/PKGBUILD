pkgname=plasma-theme-tibanna
pkgver=6.1.1.3
pkgrel=1
pkgdesc="Tibanna plasmatheme for KDE 4.x + caledonia icons"
arch=('any')
license=('GPL')
url="http://kde-look.org/content/show.php/Tibanna?content=115322"
depends=('kdelibs' 'kdebase-workspace')
source=(
	"http://kde-look.org/CONTENT/content-files/115322-Tibanna.tar.gz"
	"caledonia-icons-1.3.tar.gz::http://www.herecura.eu/files/caledonia-icons.tar.gz"
)
sha256sums=(
	'f191d891e1aa400fa26c68476b6ceca53a31bd92de23049c207a0195a74c7705'
	'b282aac8893263931a70f671275eab9c4e0783b7967c036a7b9bac9686ef4ef0'
)

build() {
	cd Tibanna
	find -name "*~" -delete
	find -name ".directory" -delete
}

package() {
  install -dm755 ${pkgdir}/usr/share/apps/desktoptheme
  cp -a ${srcdir}/Tibanna ${pkgdir}/usr/share/apps/desktoptheme/tibanna
  cp -a ${srcdir}/icons ${pkgdir}/usr/share/apps/desktoptheme/tibanna/
}
