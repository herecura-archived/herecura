# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Danilo Kuehn <dk[at]nogo-software[dot]de>

_name=packer
pkgname=packer-io
pkgver=0.7.0
pkgrel=1
pkgdesc="tool for creating identical machine images for multiple platforms from a single source configuration."
url="http://www.packer.io"
arch=('x86_64' 'i686')
license=('MPL2')
depends=('glibc')
makedepends=('git' 'go' 'mercurial')
#source=("$pkgname::git://github.com/mitchellh/packer.git#tag=v$pkgver")
#md5sums=('SKIP')

prepare() {
	export GOPATH="$srcdir/go"
	export GOROOT=$(go env GOROOT)
	export PATH="$PATH:$GOPATH/bin"

	[[ ! -d "$srcdir/go" ]] && mkdir -p "$srcdir/go"
	
	go get -u github.com/mitchellh/gox
	go get -u github.com/mitchellh/packer

	#cp -a "$srcdir/packer-io" "$srcdir/go/src/github.com/mitchellh/packer"
}

build() {
	cd "$srcdir/go/src/github.com/mitchellh/packer"

	make updatedeps
	git checkout -b v$pkgver
	make dev
}

check() {
	cd "$srcdir/go/src/github.com/mitchellh/packer"

	make test
}

package() {
	install -dm755 "${pkgdir}/usr/bin"

	cd "$srcdir/go/src/github.com/mitchellh/packer/bin"

	install -Dm755 packer "${pkgdir}/usr/bin/packer-io"
	install -Dm755 packer-* "${pkgdir}/usr/bin"

	cd "$srcdir/go/src/github.com/mitchellh/packer"
	# license
	#install -dm755 ${pkgdir}/usr/share/licenses/$pkgname
	install -Dm644 ${srcdir}/go/src/github.com/mitchellh/packer/LICENSE \
		${pkgdir}/usr/share/licenses/$pkgname/LICENSE
}
