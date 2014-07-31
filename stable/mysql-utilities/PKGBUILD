# Maintainer: Raphaël Doursenaud <rdoursenaud@free.fr>
pkgname=mysql-utilities
pkgver=1.4.4
pkgrel=1
pkgdesc="A collection of command-line utilities that are used for maintaining and administering MySQL servers"
arch=('any')
url="http://dev.mysql.com/downloads/tools/utilities/"
license=('GPL')
depends=('python2' 'python2-sphinx' 'python2-jinja' 'python2-mysql-connector')
options=(!emptydirs)
source=(http://cdn.mysql.com/Downloads/MySQLGUITools/$pkgname-$pkgver.tar.gz)

package() {
	cd "$srcdir/$pkgname-$pkgver"
	python2 setup.py install --root="$pkgdir/" --optimize=1

	# Remove files clashing with python2-mysql-connector
	rm -f "$pkgdir/usr/lib/python2.7/site-packages/mysql/__init__.py"
	rm -f "$pkgdir/usr/lib/python2.7/site-packages/mysql/__init__.pyc"
	rm -f "$pkgdir/usr/lib/python2.7/site-packages/mysql/__init__.pyo"
}
sha256sums=('8dd86095ce2736d3adbccdc1eed3f4a3ad1377bc8af445198db553ab6db9e8f6')
