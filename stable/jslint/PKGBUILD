# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>

pkgname=jslint
_npmname=jslint
pkgver=0.6.1
pkgrel=1
pkgdesc="The JavaScript Code Quality Tool"
arch=('any')
depends=('nodejs')
url="http://jslint.com/"
license=('MIT')
provides=('nodejs-jslint')

package() {
	local _npmdir="$pkgdir/usr/lib/node_modules/"
	mkdir -p $_npmdir
	cd $_npmdir
	npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$pkgver
}
sha256sums=()
