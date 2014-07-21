pkgname=davmail
_pkgver=4.5.1
_rev=2303
pkgver=4.5.1.2303
pkgrel=1
pkgdesc="a POP/IMAP/SMTP/Caldav/LDAP gateway for the exchange service"
arch=('i686' 'x86_64')
url="http://davmail.sourceforge.net/"
license=('GPL')
makedepends=('apache-ant')
depends=('java-runtime')
source=(
	"http://downloads.sourceforge.net/project/$pkgname/$pkgname/$_pkgver/$pkgname-src-$_pkgver-$_rev.tgz"
)
install=davmail.install

build() {
	cd "$pkgname-src-$_pkgver-$_rev"
	ANT_OPTS=-Dfile.encoding=UTF-8 ant
}

package() {
	cd "$pkgname-src-$_pkgver-$_rev"
	install -dm755 "$pkgdir/usr/share/java/$pkgname"
	cd dist
	if [ "$CARCH" = "i686" ]; then
		bsdtar --strip-components 1 -xf $pkgname-linux-x86-$_pkgver-trunk.tgz -C "$pkgdir/usr/share/java/$pkgname/"
	elif [ "$CARCH" = "x86_64" ]; then
		bsdtar --strip-components 1 -xf $pkgname-linux-x86_64-$_pkgver-trunk.tgz -C "$pkgdir/usr/share/java/$pkgname/"
	fi
	# Create icons
	cd "$srcdir/$pkgname-src-$_pkgver-$_rev"
	install -Dm644 src/java/tray2.png ${pkgdir}/usr/share/icons/hicolor/16x16/apps/davmail.png
	install -Dm644 src/java/tray32.png ${pkgdir}/usr/share/icons/hicolor/32x32/apps/davmail.png
	install -Dm644 src/java/tray48.png ${pkgdir}/usr/share/icons/hicolor/48x48/apps/davmail.png

	# fix davmail.sh so it uses realpath
	sed -e 's,`dirname $0`,$(dirname $(realpath $0)),' -i "$pkgdir/usr/share/java/$pkgname/davmail.sh"

	# bin
	install -dm755 "$pkgdir/usr/bin"
	ln -sf "/usr/share/java/$pkgname/davmail.sh" "$pkgdir/usr/bin/davmail"

	# dektop
	# fix icon
	sed -e 's,^Icon=.*,Icon=davmail,' -i dist/$pkgname.desktop
	# install
	install -Dm644 dist/$pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
}

sha256sums=('2621a5cbc81c06d0345ec05c93664a052e2e9d2d2bfda8e731a8fb94fd70f752')
