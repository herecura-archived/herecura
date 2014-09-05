# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Mathieu Clabaut <mathieu.clabaut@gmail.com>
# Contributor: helios <aur@wiresphere.de>
pkgname=vagrant
pkgver=1.6.5
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
[[ "$CARCH" == "i686" ]] && sha256sums=('997f69514d28919c00d32538b833d89e92c384b85b07ac0cc241c311bf82a454')
[[ "$CARCH" == "x86_64" ]] && sha256sums=('90730fd10cbd811969ec58f28818685f3074f8399852dfd1d4858d75c4224fdc')

sha256sums+=(
	'e4b8a4b4292472033a08b20e4daf5eb62c21c50b491c34ddac9792fec40aac48'
)

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
