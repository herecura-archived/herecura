# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: (sirocco AT ngs.ru)

pkgbase=doublecmd-svn
pkgname=('doublecmd-svn-gtk2' 'doublecmd-svn-qt')
pkgver=4871
pkgrel=1
url="http://doublecmd.sourceforge.net/"
arch=('i686' 'x86_64')
license=('GPL')
install="$pkgbase.install"
provides=('doublecmd')
conflicts=('doublecmd')
makedepends=('lazarus' 'qt4pas' 'gtk2' 'subversion')
optdepends=('lua: scripting' 'p7zip: support for 7zip archives' 'libunrar: support for rar archives' 'zip: support for zip files' 'unzip: support for zip files')
source=()

_svntrunk=http://doublecmd.svn.sourceforge.net/svnroot/doublecmd/trunk
_svnmod=doublecmd

build() {
	if [ -d $_svnmod/.svn ]; then
		cd $_svnmod && svn up -r $pkgver
		cd "$srcdir"
	else
		svn co $_svntrunk --config-dir ./ $_svnmod
	fi
	msg "SVN checkout done or server timeout"
	msg "Starting make..."

	[ -d $pkgbase-gtk ] && rm -rf $pkgbase-gtk
	[ -d $pkgbase-qt  ] && rm -rf $pkgbase-qt

	cp -a $_svnmod $pkgbase-gtk
	cp -a $_svnmod $pkgbase-qt

	cd "$srcdir/$pkgbase-gtk"
	./build.sh beta gtk2

	cd "$srcdir/$pkgbase-qt"
	./build.sh beta qt
}

package_doublecmd-svn-gtk2() {
	pkgdesc="twin-panel (commander-style) file manager (GTK)"
	depends=('gtk2')
	cd "$srcdir/$pkgbase-gtk"
	sed -e 's/LIB_SUFFIX=.*/LIB_SUFFIX=/g' -i ./install/linux/install.sh
	./install/linux/install.sh --install-prefix="$pkgdir"
}

package_doublecmd-svn-qt() {
	pkgdesc="twin-panel (commander-style) file manager (QT)"
	depends=('qt4pas')
	cd "$srcdir/$pkgbase-qt"
	sed -e 's/LIB_SUFFIX=.*/LIB_SUFFIX=/g' -i ./install/linux/install.sh
	./install/linux/install.sh --install-prefix="$pkgdir"
}
