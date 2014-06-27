# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Mathieu Clabaut <mathieu.clabaut@gmail.com>
# Contributor: helios <aur@wiresphere.de>
pkgname=vagrant
pkgver=1.6.3
pkgrel=2
pkgdesc="Tool for building and distributing virtualized development environments"
arch=('i686' 'x86_64')
url="http://vagrantup.com/"
license=('MIT')
options=(!strip)
optdepends=('net-tools: NFS shared folder support')
source=(
	"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_${CARCH}.rpm"
	'zsh-vagrant'
	'0001-Arch-Linux-nfs-service-files-changed.patch'
)
#source=(
	#"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_i686.rpm"
	#"https://dl.bintray.com/mitchellh/${pkgname}/${pkgname}_${pkgver}_x86_64.rpm"
#)
[[ "$CARCH" == "i686" ]] && sha256sums=('b0e3a8641853111990ac39ad05158339400ee56c3d8fbab3704b1e1be5c0bd51')
[[ "$CARCH" == "x86_64" ]] && sha256sums=('e4d6318a0d204818f3742f3280f3150d51b613e96a457cae4d0ea16c84be9fd3')

sha256sums+=(
	'b4a14cbcb8d2148f179241d8b7cbb418f9ac50680cfe2541cb3570b9824efad5'
	'f9231042bc981be1f1e3828d5bb2827c29916dd443235ba35915c974851a7ee8'
)

package() {
	mv $srcdir/{opt,usr} $pkgdir

	# fix nfs service names
	(
		cd $pkgdir/opt/vagrant/embedded/gems/gems/vagrant-${pkgver}
		patch -Np1 -i $srcdir/0001-Arch-Linux-nfs-service-files-changed.patch
	)

	# zsh completion
	install -dm0755 "${pkgdir}/usr/share/zsh/site-functions"
	install -m0644 ${srcdir}/zsh-vagrant "${pkgdir}/usr/share/zsh/site-functions/_vagrant"

	# bash completion
	install -dm0755 "${pkgdir}/usr/share/bash-completion/completions"
	ln -sf "/opt/$pkgname/embedded/gems/gems/$pkgname-$pkgver/contrib/bash/completion.sh" \
		"${pkgdir}/usr/share/bash-completion/completions/vagrant"
}
