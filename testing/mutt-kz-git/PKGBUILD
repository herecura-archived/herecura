# vim:set ft=sh:
# Contributor: boyska <piuttosto@logorroici.org>

pkgname=mutt-kz-git
_gitname=muttkz
pkgver=20131113.6b67584
pkgrel=1
pkgdesc="A small but very powerful text-based mail client + integration with notmuch"
url="https://github.com/karelzak/mutt-kz"
arch=('i686' 'x86_64')
license=('GPL')
depends=('openssl>=0.9.8e' 'gdbm' 'mime-types' 'zlib' 'libsasl' 'gpgme' 'ncurses' 'notmuch' 'libidn')
makedepends=('git' 'gnupg' 'libxslt')
conflicts=('mutt')
provides=('mutt')
#options=('!strip')
source=("$_gitname::git://github.com/karelzak/mutt-kz.git")
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/$_gitname"
	echo $(git log -1 --format="%ci" | sed 's/.*\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\).*/\1\2\3/').$(git rev-parse --short HEAD)
}

build() {
	rm -rf "$srcdir/$_gitname-build"
	/usr/share/git/workdir/git-new-workdir ${_gitname} ${_gitname}-build master
	cd "$srcdir/$_gitname-build"

	sed -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' -i configure.ac
	./prepare \
		--prefix=/usr \
		--sysconfdir=/etc \
		--enable-debug \
		--enable-gpgme \
		--enable-hcache \
		--enable-imap \
		--enable-notmuch \
		--enable-pgp \
		--enable-pop \
		--enable-smtp \
		--with-idn \
		--with-sasl \
		--with-ssl=/usr \
		--with-regex
	make
}

package() {
	cd "$srcdir/$_gitname-build"
	make DESTDIR="$pkgdir/" install
	rm -f ${pkgdir}/etc/mime.types*
	install -Dm644 contrib/gpg.rc ${pkgdir}/etc/Muttrc.gpg.dist
}
