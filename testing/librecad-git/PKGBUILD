# vim:set ft=sh:
# Maintainer: mickele <mimocciola at yahoo dot com>
# Contributor: BlackEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Ilmari Repo <ilmari at gmail dot com> (librecad-svn PKGBUILD)
# Contributor: GazJ Gary James <garyjames82 at gmail dot com> (CADuntu PKGBUILD)

pkgname=librecad-git
_gitname="librecad"
pkgver=20140727.15b103e
pkgrel=1
pkgdesc="A 2D CAD drawing tool based on the community edition of QCad."
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/librecad/"
license=('GPL')
depends=('qt4' 'boost-libs')
makedepends=('git' 'boost' 'muparser')
provides=('librecad')
replaces=('librecad-svn' 'caduntu' 'caduntu-svn')
source=("$_gitname::git://github.com/LibreCAD/LibreCAD.git")
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/$_gitname"
	echo $(git log -1 --format="%ci" | sed 's/.*\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\).*/\1\2\3/').$(git rev-parse --short HEAD)
}

build() {
	msg "Starting make..."
	cd $_gitname

	export PATH="/usr/lib/qt4/bin:${PATH}"
	qmake-qt4 librecad.pro
	make

	(
		cd plugins
		for _qtpro in $(find -name "*.pro"); do
			sed -e 's/\/src\/plugins/\/librecad\/src\/plugins/' -i $_qtpro
		done
		qmake-qt4
		make
	)
}

package() {
	cd $_gitname
	install -Dm 755 unix/librecad "$pkgdir/usr/bin/librecad"
	install -Dm 755 unix/ttf2lff "$pkgdir/usr/bin/ttf2lff"
	install -Dm 644 desktop/librecad.desktop "$pkgdir/usr/share/applications/librecad.desktop"
	install -Dm 644 librecad/res/main/librecad.png "$pkgdir/usr/share/pixmaps/librecad.png"
	mkdir -p "$pkgdir/usr/share/librecad/"
	cp -r unix/resources/{library,patterns,fonts,qm,doc} "$pkgdir/usr/share/librecad/"
	mkdir -p "$pkgdir/usr/lib/librecad/"
	cp -r unix/resources/plugins "$pkgdir/usr/lib/librecad/"
}
