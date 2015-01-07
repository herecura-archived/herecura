# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Mathieu Clabaut <mathieu.clabaut@gmail.com>
# Contributor: helios <aur@wiresphere.de>
pkgname=vagrant
pkgver=1.7.2
pkgrel=1
pkgdesc="Tool for building and distributing virtualized development environments"
arch=('i686' 'x86_64')
url="http://vagrantup.com/"
license=('MIT')
options=(!strip)
optdepends=('net-tools: NFS shared folder support')
source=(
	"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_i686.rpm"
	"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_x86_64.rpm"
	'zsh-vagrant'
)
noextract=(
	"${pkgname}_${pkgver}_i686.rpm"
	"${pkgname}_${pkgver}_x86_64.rpm"
)

prepare() {
	bsdcpio -id < "${pkgname}_${pkgver}_${CARCH}.rpm"
}

package() {
	mv $srcdir/{opt,usr} $pkgdir

	# zsh completion
	install -dm0755 "${pkgdir}/usr/share/zsh/site-functions"
	install -m0644 ${srcdir}/zsh-vagrant "${pkgdir}/usr/share/zsh/site-functions/_vagrant"

	# bash completion
	install -dm0755 "${pkgdir}/usr/share/bash-completion/completions"
	ln -sf "/opt/$pkgname/embedded/gems/gems/$pkgname-$pkgver/contrib/bash/completion.sh" \
		"${pkgdir}/usr/share/bash-completion/completions/vagrant"
}

sha256sums=('cf822183e8c883f58e3860edd434c0406efa8d11e6d1e67249a295b55a0f655d'
            '2ec53d71baf13a3561311026b81b2704fe752870d9cba86d02e2ae3930ba754d'
            'e4b8a4b4292472033a08b20e4daf5eb62c21c50b491c34ddac9792fec40aac48')
