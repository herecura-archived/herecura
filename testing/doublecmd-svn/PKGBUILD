# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: (sirocco AT ngs.ru)

pkgbase=doublecmd-svn
_svnmod=doublecmd
pkgname=('doublecmd-svn-gtk2' 'doublecmd-svn-qt')
pkgver=5455
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

build() {
	[ -d $pkgbase-gtk ] && rm -rf $pkgbase-gtk
	[ -d $pkgbase-qt  ] && rm -rf $pkgbase-qt

	cp -a $_svnmod $pkgbase-gtk
	cp -a $_svnmod $pkgbase-qt

	cd "$srcdir/$pkgbase-gtk"
	# dont use fPIC on i686
	if [ "$CARCH" = "i686" ]; then
		sed -e '/fPIC/d' -i "$srcdir/$pkgbase-gtk/components/doublecmd/doublecmd_common.lpk"
	fi
	sed -e 's/\(export\ lazbuild=\).*/\1"$(which\ lazbuild) --lazarusdir=\/usr\/lib\/lazarus"/' -i build.sh
	./build.sh beta gtk2

	cd "$srcdir/$pkgbase-qt"
	# dont use fPIC on i686
	if [ "$CARCH" = "i686" ]; then
		sed -e '/fPIC/d' -i "$srcdir/$pkgbase-qt/components/doublecmd/doublecmd_common.lpk"
	fi
	sed -e 's/\(export\ lazbuild=\).*/\1"$(which\ lazbuild) --lazarusdir=\/usr\/lib\/lazarus"/' -i build.sh
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
