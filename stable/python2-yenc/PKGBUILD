# Contributor: Jonathan Curran <jonc@icicled.net>
# Maintainer: Clément Démoulins <clement@archivel.fr>

pkgname=python2-yenc
pkgver=0.4.0
pkgrel=2
arch=('i686' 'x86_64')
license=('GPL')
pkgdesc='yenc decoder for python2'
url='http://www.golug.it/yenc.html'
depends=('python2')
source=("http://www.golug.it/pub/yenc/${pkgname/python2-/}-$pkgver.tar.gz")
source=("$pkgname-$pkgver.tar.bz2::https://bitbucket.org/dual75/yenc/get/$pkgver.tar.bz2")

package() {
	cd dual75-yenc-$pkgver
	python2 setup.py install --root="$pkgdir"
}
sha256sums=('32f04bfaaabf2e255138d4c9b418581f2d8d093e831f872aa19fbd895f3c5fee')
