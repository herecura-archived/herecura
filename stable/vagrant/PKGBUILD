# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Mathieu Clabaut <mathieu.clabaut@gmail.com>
# Contributor: helios <aur@wiresphere.de>
pkgname=vagrant
pkgver=1.4.3
pkgrel=1
pkgdesc="Tool for building and distributing virtualized development environments"
arch=('i686' 'x86_64')
url="http://vagrantup.com/"
license=('MIT')
options=(!strip)
optdepends=('net-tools: NFS shared folder support')
source=(
	"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_${CARCH}.rpm"
	'zsh-vagrant'
)
#source=(
	#"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_i686.rpm"
	#"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_x86_64.rpm"
#)
[[ "$CARCH" == "i686" ]] && sha256sums=('68d4673fe7657cc8d075412f57a19c878a6e187b2f2fc54462e5ac3041d912fe')
[[ "$CARCH" == "x86_64" ]] && sha256sums=('a2057895601f46db4de22832ac462ee63e07e9905c1bfd11318290bd362137f9')

sha256sums+=('2291ab476e34bb5c44e49a6064e02478c00fd99d1a6da7b11b25cd217c3df1d7')

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
