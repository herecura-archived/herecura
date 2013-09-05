# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Mathieu Clabaut <mathieu.clabaut@gmail.com>
# Contributor: helios <aur@wiresphere.de>
pkgname=vagrant
pkgver=1.3.0
pkgrel=1
pkgdesc="Tool for building and distributing virtualized development environments"
arch=('i686' 'x86_64')
url="http://vagrantup.com/"
license=('MIT')
options=(!strip)
depends=
_git_revision='0224c6232394680971a69d94dd55a7436888c4cb'
source=(
	"http://files.vagrantup.com/packages/${_git_revision}/${pkgname}_${pkgver}_${CARCH}.rpm"
	"zsh-vagrant"
	"bash-vagrant"
)
#source=(
	#"http://files.vagrantup.com/packages/${_git_revision}/${pkgname}_${pkgver}_i686.rpm"
	#"http://files.vagrantup.com/packages/${_git_revision}/${pkgname}_${pkgver}_x86_64.rpm"
#)
[[ "$CARCH" == "i686" ]] && md5sums=('325b031ebf0d6cbb7ba5ff295802c3a8')
[[ "$CARCH" == "x86_64" ]] && md5sums=('17bdde43ab35efb4e574cfdb345d5422')

md5sums+=('dd7605a4a60732d9c1715cab9b93e120' 'c41db06a3282b89aed96ad37b76c69b2')

package() {
	mv $srcdir/{opt,usr} $pkgdir

	# zsh completion
	install -dm0755 "${pkgdir}/usr/share/zsh/site-functions"
	install -m0644 ${srcdir}/zsh-vagrant "${pkgdir}/usr/share/zsh/site-functions/_vagrant"

	# bash completion
	install -dm0755 "${pkgdir}/usr/share/bash-completion/completions"
	install -m0644 ${srcdir}/bash-vagrant "${pkgdir}/usr/share/bash-completion/completions/vagrant"
}
