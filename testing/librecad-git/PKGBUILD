# Maintainer: mickele <mimocciola at yahoo dot com>
# Contributor: BlackEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Ilmari Repo <ilmari at gmail dot com> (librecad-svn PKGBUILD)
# Contributor: GazJ Gary James <garyjames82 at gmail dot com> (CADuntu PKGBUILD)

pkgname=librecad-git
pkgver=20120310
pkgrel=1
pkgdesc="A 2D CAD drawing tool based on the community edition of QCad."
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/librecad/"
license=('GPL')
depends=('qt' 'boost-libs')
makedepends=('git' 'boost')
provides=('librecad')
replaces=('librecad-svn' 'caduntu' 'caduntu-svn')
source=()
md5sums=()

if [ -e .githash_${CARCH} ] ; then
	_gitphash=$(cat .githash_${CARCH})
else
	_gitphash=""
fi

_gitname="librecad"
_gitroot="git://github.com/LibreCAD/LibreCAD.git"

build() {
	if [ -d ${srcdir}/${_gitname}/.git ] ; then
		( cd ${srcdir}/${_gitname} && git pull origin )
		msg "The local files are updated."
	else
		( git clone --depth 1 ${_gitroot} ${_gitname} )
	fi
	msg "GIT checkout done or server timeout"

	cd ${_gitname}
	if [ "${_gitphash}" == $(git show | grep -m 1 commit | sed 's/commit //') ]; then
		msg "Git hash is the same as previous build"
		return 1
	fi

	msg "creating build directory"
	cd ${srcdir}
	[ -d ${_gitname}-build ] && rm -rf ${_gitname}-build
	cp -a ${_gitname} ${_gitname}-build

	msg "Starting make..."
	cd ${_gitname}-build

	qmake librecad.pro
	make

	#(
		#cd plugins
		#for _qtpro in $(find -name "*.pro"); do
			#sed -e 's/\/src\/plugins/\/librecad\/src\/plugins/' -i ${_qtpro}
		#done
		#qmake
		#make
	#)
}

package() {
	cd ${_gitname}-build
	install -D -m 755 unix/librecad $pkgdir/usr/bin/librecad
	install -D -m 644 desktop/librecad.desktop ${pkgdir}/usr/share/applications/librecad.desktop
	install -D -m 644 librecad/res/main/librecad.png ${pkgdir}/usr/share/pixmaps/librecad.png
	mkdir -p ${pkgdir}/usr/share/librecad/
	cp -r unix/resources/{library,patterns,fonts,qm,doc} ${pkgdir}/usr/share/librecad/
	#mkdir -p ${pkgdir}/usr/lib/librecad/
	#cp -r unix/resources/plugins ${pkgdir}/usr/lib/librecad/
	git show | grep -m 1 commit | sed 's/commit //' > ${startdir}/.githash_${CARCH}
}
