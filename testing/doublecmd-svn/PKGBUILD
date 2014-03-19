# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: (sirocco AT ngs.ru)

pkgbase=doublecmd-svn
_svnmod=doublecmd
pkgname=('doublecmd-svn-gtk2' 'doublecmd-svn-qt')
pkgver=5480
pkgrel=1
url="http://doublecmd.sourceforge.net/"
arch=('i686' 'x86_64')
license=('GPL')
install="$pkgbase.install"
provides=('doublecmd')
conflicts=('doublecmd')
makedepends=('lazarus' 'qt4pas' 'gtk2' 'subversion')
optdepends=('lua51: scripting' 'p7zip: support for 7zip archives' 'libunrar: support for rar archives' 'zip: support for zip files' 'unzip: support for zip files')
source=("$_svnmod::svn://svn.code.sf.net/p/doublecmd/code/trunk")
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/$_svnmod"
	svnversion | tr -d [A-z]
}

prepare() {
	cd "$srcdir/$_svnmod"
	sed -e 's/\(export\ lazbuild=\).*/\1"$(which\ lazbuild) --lazarusdir=\/usr\/lib\/lazarus"/' -i build.sh
	#sed -e 's/LIB_SUFFIX=.*/LIB_SUFFIX=/g' -i ./install/linux/install.sh
}

build() {
	[ -d $pkgbase-gtk ] && rm -rf $pkgbase-gtk
	[ -d $pkgbase-qt  ] && rm -rf $pkgbase-qt

	cp -a $_svnmod $pkgbase-gtk
	cp -a $_svnmod $pkgbase-qt

	cd "$srcdir/$pkgbase-gtk"
	./build.sh all gtk2

	cd "$srcdir/$pkgbase-qt"
	./build.sh all qt
}

package_doublecmd-svn-gtk2() {
	pkgdesc="twin-panel (commander-style) file manager (GTK)"
	depends=('gtk2')
	cd "$srcdir/$pkgbase-gtk"
	./install/linux/install.sh --install-prefix="$pkgdir"
}

package_doublecmd-svn-qt() {
	pkgdesc="twin-panel (commander-style) file manager (QT)"
	depends=('qt4pas')
	cd "$srcdir/$pkgbase-qt"
	./install/linux/install.sh --install-prefix="$pkgdir"
}
