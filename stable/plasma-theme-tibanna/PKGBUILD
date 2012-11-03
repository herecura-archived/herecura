pkgname=plasma-theme-tibanna
pkgver=6.1.0.8.1
pkgrel=1
pkgdesc="Tibanna plasmatheme for KDE 4.x + krayscale tray icons"
arch=('any')
license=('GPL')
url="http://kde-look.org/content/show.php/Tibanna?content=115322"
depends=('kdelibs' 'kdebase-workspace')
source=(
	"http://kde-look.org/CONTENT/content-files/115322-Tibanna.tar.gz"
	"http://kde-look.org/CONTENT/content-files/133300-krayscale_0.8.1.tar.gz"
)
sha256sums=(
	'f191d891e1aa400fa26c68476b6ceca53a31bd92de23049c207a0195a74c7705'
	'ae7c1022ca4503541bc7ee1efa885c44a0c49900f06a24d3610803e9c2eab256'
)

build() {
	cd Tibanna
	find -name "*~" -delete
	find -name ".directory" -delete
}

package() {
  install -dm755 ${pkgdir}/usr/share/apps/desktoptheme
  cp -a ${srcdir}/Tibanna ${pkgdir}/usr/share/apps/desktoptheme/tibanna
  cp -a ${srcdir}/krayscale_0.8.1/plasmatheme/icons ${pkgdir}/usr/share/apps/desktoptheme/tibanna/icons
}
