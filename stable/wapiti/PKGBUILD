# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >
pkgname=wapiti
pkgver=2.3.0
pkgrel=1
pkgdesc="Wapiti is a vulnerability scanner for web applications."
url='http://wapiti.sourceforge.net/'
license=('GPL')
depends=('python2-requests' 'python2-beautifulsoup3')
makedepends=('python2-setuptools')
arch=('any')

source=("http://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver.tar.gz")

package() {
	cd "$pkgname-$pkgver"
	python2 setup.py install --root="$pkgdir/" --optimize=1
}

sha256sums=('6b836a4810f17b7eda4345fb12293112129961ba243140c72a8da0ac2572f4b4')
