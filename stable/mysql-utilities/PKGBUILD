# Maintainer: Raphaël Doursenaud <rdoursenaud@free.fr>
pkgname=mysql-utilities
pkgver=1.4.3
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
sha256sums=('785f7b78ba73280c6598f63bc052a88a7e97786566dae787a5457f039864dcb7')
