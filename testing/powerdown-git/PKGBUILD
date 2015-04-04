# Maintainer: tailinchu <use_my_id at gmail dot com>

pkgname=powerdown-git
_gitname="powerdown"
pkgver=20150403.8b95050
pkgrel=1
pkgdesc="simple linux powersaving script (git version)"
arch=('any')
url="http://github.com/taylorchu/powerdown"
license=('GPL2')
depends=('bash' 'iw' 'ethtool' 'hdparm' 'bc' 'x86_energy_perf_policy')
makedepends=('git')
conflicts=('pm-utils')
provides=('pm-utils')
source=("$_gitname::git://github.com/taylorchu/powerdown.git")
md5sums=('SKIP')


pkgver () {
    cd "$srcdir/$_gitname"
	git log -1 --date=short --format="%cd.%h" | tr -d '-'
}

package() {
    cd "$srcdir/$_gitname"
    make PREFIX=/usr DESTDIR="$pkgdir" install
}

