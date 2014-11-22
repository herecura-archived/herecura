# vim:set ft=sh:
# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Thomas Baechler <thomas@archlinux.org>

_kernelname=-bede
pkgbase="linux$_kernelname"
pkgname=("linux$_kernelname" "linux$_kernelname-headers")
_basekernel=3.17
_patchver=4
if [[ "$_patchver" == rc* ]]; then
	# rc kernel
	_baseurl='https://www.kernel.org/pub/linux/kernel/v3.x/testing'
	pkgver=${_basekernel}$_patchver
	_linuxname="linux-${_basekernel}-$_patchver"
else
	# $_patchver is no RC build normal
	_baseurl='https://www.kernel.org/pub/linux/kernel/v3.x'
	pkgver=$_basekernel
	_linuxname="linux-$_basekernel"
fi
pkgrel=2
arch=('i686' 'x86_64')
license=('GPL2')
makedepends=('bc' 'kmod' 'clang')
url="http://www.kernel.org"
options=(!strip)

source=(
	"$_baseurl/$_linuxname.tar.xz"
	# the main kernel config files
	"config-desktop.i686"
	"config-desktop.x86_64"
	# standard config files for mkinitcpio ramdisk
	"linux$_kernelname.preset"
	# sysctl tweaks
	'sysctl-linux-bede.conf'
)
sha256sums=(
	'f5153ec93c5fcd41b247950e6a9bcbc63fa87beafd112c133a622439a0f76251'
	'14cd296a42457c8814818e19fdc2b1441981141969c2abe2cf2f3a06704fb8ee'
	'f1b5e361356eec1be584cd055b8d976e404feb105c5f51b9b5fb7f11fe9f17cd'
	'd5bb4aabbd556f8a3452198ac42cad6ecfae020b124bcfea0aa7344de2aec3b5'
	'e939ae473776190eb327e3afd5315626d6ac87a84b5475e08979c319e917a1d4'
)

# revision patches
if [[ "$_patchver" =~ ^[0-9]*$ ]]; then
	if [[ $_patchver -ne 0 ]]; then
	pkgver=$_basekernel.$_patchver
	_patchname="patch-$pkgver"
	source=( "${source[@]}"
		"$_baseurl/$_patchname.xz"
	)
	sha256sums=( "${sha256sums[@]}"
		'eeef37397a15245bd143569908be40622a87dc7673965e623e811ea3f68b8434'
	)
	fi
fi

## extra patches
_extrapatches=(
)
_extrapatchessums=(
)
if [[ ${#_extrapatches[@]} -ne 0 ]]; then
	source=( "${source[@]}"
		"${_extrapatches[@]}"
	)
	sha256sums=( "${sha256sums[@]}"
		"${_extrapatchessums[@]}"
	)
fi

export HOSTCC=clang
export CC=clang
export CXX=clang++

prepare() {
	# check signatures
	curl -O "$_baseurl/${_linuxname}.tar.sign"
	xz -cd ${_linuxname}.tar.xz | gpg --verify ${_linuxname}.tar.sign -

	if [[ "$_patchver" =~ ^[0-9]+$ ]]; then
		if [[ ${_patchver} -ne 0 ]]; then
			curl -O "$_baseurl/${_patchname}.sign"
		gpg --verify ${_patchname}.sign
		fi
	fi

	cd "$srcdir/$_linuxname"

	# Add revision patches
	if [[ "$_patchver" =~ ^[0-9]+$ ]]; then
		if [[ $_patchver -ne 0 ]]; then
			msg2 "apply $_patchname"
			patch -Np1 -i "$srcdir/$_patchname"
		fi
	fi

	# extra patches
	for patch in ${_extrapatches[@]}; do
		patch="$(basename "$patch" | sed -e 's/\.\(gz\|bz2\|xz\)//')"
		msg2 "apply $patch"
		patch -Np1 -i "$srcdir/$patch"
	done

	# set configuration
	msg2 "copy configuration"
	if [[ "$CARCH" = "x86_64" ]]; then
		cat "$srcdir/config-desktop.x86_64" >./.config
	else
		cat "$srcdir/config-desktop.i686" >./.config
	fi
	if [[ "$_kernelname" != "" ]]; then
		sed -i "s|CONFIG_LOCALVERSION=.*|CONFIG_LOCALVERSION=\"\U$_kernelname\"|g" ./.config
	fi

	# set extraversion to pkgrel
	msg2 "set extraversion to $pkgrel"
	if [[ "$_patchver" == rc* ]]; then
		sed -ri "s|^(EXTRAVERSION =).*|\1 ${_patchver}-$pkgrel|" Makefile
	else
		sed -ri "s|^(EXTRAVERSION =).*|\1 -$pkgrel|" Makefile
	fi

	# don't run depmod on 'make install'. We'll do this ourselves in packaging
	sed -i '2iexit 0' scripts/depmod.sh

	# hack to prevent output kernel from being marked as dirty or git
	msg2 "apply hack to prevent kernel tree being marked dirty"
	echo "" > "$srcdir/$_linuxname/.scmversion"
}

build() {
	cd "$srcdir/$_linuxname"

	msg2 "prepare"
	make prepare
	# load configuration
	# Configure the kernel. Replace the line below with one of your choice.
	#make menuconfig # CLI menu for configuration
	#make xconfig # X-based configuration
	#make oldconfig # using old config from previous kernel version
	# ... or manually edit .config
	####################
	# stop here
	# this is useful to configure the kernel
	#msg "Stopping build"
	#return 1
	####################
	# yes "" | make config
	# build!
	msg2 "build"
	make $MAKEFLAGS bzImage modules
}

package_linux-bede() {
	pkgdesc="The Linux Kernel and modules, BlackEagle Desktop Edition"
	provides=('linux')
	backup=(
		"etc/mkinitcpio.d/$pkgname.preset"
	)
	depends=('coreutils' 'kmod>=10' 'mkinitcpio>=0.9')
	optdepends=(
		'crda: to set the correct wireless channels of your country'
		'linux-firmware: when having some hardware needing special firmware'
	)
	replaces=(
		'nouveau-drm' 'kernel26-slk' "kernel26$_kernelname" "linux-bemm"
	)

	install=$pkgname.install

	KARCH=x86
	cd "$srcdir/$_linuxname"

	mkdir -p "$pkgdir"/{lib/modules,lib/firmware,boot,usr}

	# get kernel version
	_kernver=$(make kernelrelease)

	# install modules
	make INSTALL_MOD_STRIP=1 INSTALL_MOD_PATH="$pkgdir" modules_install

	# copy System.map and bzImage
	install -m644 System.map "$pkgdir/boot/System.map$_kernelname"
	install -m644 arch/$KARCH/boot/bzImage "$pkgdir/boot/vmlinuz$_kernelname"

	# install fallback mkinitcpio.conf file and preset file for kernel
	install -m644 -D "$srcdir/$pkgname.preset" "$pkgdir/etc/mkinitcpio.d/$pkgname.preset"

	# set correct depmod command for install
	sed \
		-e  "s/KERNEL_NAME=.*/KERNEL_NAME=$_kernelname/g" \
		-e  "s/KERNEL_VERSION=.*/KERNEL_VERSION=$_kernver/g" \
		-i "$startdir/$pkgname.install"
	sed \
		-e "s|source .*|source /etc/mkinitcpio.d/$pkgname.kver|g" \
		-e "s|default_image=.*|default_image=\"/boot/initramfs$_kernelname.img\"|g" \
		-e "s|fallback_image=.*|fallback_image=\"/boot/initramfs$_kernelname-fallback.img\"|g" \
		-i "$pkgdir/etc/mkinitcpio.d/$pkgname.preset"

	echo -e "# DO NOT EDIT THIS FILE\nALL_kver='$_kernver'" > "$pkgdir/etc/mkinitcpio.d/$pkgname.kver"

	# remove build and source links
	rm -f "$pkgdir/lib/modules/$_kernver"/{source,build}

	# remove the firmware
	rm -rf "$pkgdir/lib/firmware"

	_fldkernelname=$(echo $_kernelname | tr "[:lower:]" "[:upper:]")
	# make room for external modules
	ln -s "../${_basekernel}$_fldkernelname-external" "$pkgdir/lib/modules/$_kernver/external"
	# add real version for building modules and running depmod from post_install/upgrade
	mkdir -p "$pkgdir/lib/modules/$_basekernel$_fldkernelname-external"
	echo "$_kernver" > "$pkgdir/lib/modules/${_basekernel}$_fldkernelname-external/version"

	# gzip all modules
	find "$pkgdir" -name '*.ko' -exec gzip -9 {}  \;

	# Now we call depmod...
	depmod -b "$pkgdir" -F System.map "$_kernver"

	# move module tree /lib -> /usr/lib
	mv "$pkgdir/lib" "$pkgdir/usr/"

	# install sysctl tweaks
	install -Dm644 "$srcdir/sysctl-linux-bede.conf" "$pkgdir/usr/lib/sysctl.d/60-linux-bede.conf"
}

package_linux-bede-headers() {
	pkgdesc="Header files and scripts for building modules for linux$_kernelname"
	provides=('linux-headers')
	replaces=("kernel26$_kernelname-headers" "linux-bemm-headers")
	install -dm755 "$pkgdir/usr/lib/modules/$_kernver"
	cd "$pkgdir/usr/lib/modules/$_kernver"
	ln -sf ../../../src/linux-$_kernver build
	cd "$srcdir/$_linuxname"
	install -D -m644 Makefile \
		"$pkgdir/usr/src/linux-$_kernver/Makefile"
	install -D -m644 kernel/Makefile \
		"$pkgdir/usr/src/linux-$_kernver/kernel/Makefile"
	install -D -m644 .config \
		"$pkgdir/usr/src/linux-$_kernver/.config"

	# copy files necessary for later builds, like nvidia and vmware
	cp Module.symvers "$pkgdir/usr/src/linux-$_kernver"
	cp -a scripts "$pkgdir/usr/src/linux-$_kernver"
	# fix permissions on scripts dir
	chmod og-w -R "$pkgdir/usr/src/linux-$_kernver/scripts"
	mkdir -p "$pkgdir/usr/src/linux-$_kernver/.tmp_versions"

	mkdir -p "$pkgdir/usr/src/linux-$_kernver/arch/$KARCH/kernel"

	cp arch/$KARCH/Makefile "$pkgdir/usr/src/linux-$_kernver/arch/$KARCH/"
	if [[ "$CARCH" = "i686" ]]; then
		cp arch/$KARCH/Makefile_32.cpu "$pkgdir/usr/src/linux-$_kernver/arch/$KARCH/"
	fi
	cp arch/$KARCH/kernel/asm-offsets.s "$pkgdir/usr/src/linux-$_kernver/arch/$KARCH/kernel/"

	# add docbook makefile
	install -D -m644 Documentation/DocBook/Makefile \
		"$pkgdir/usr/src/linux-$_kernver/Documentation/DocBook/Makefile"

	# add config
	for config in `find ./include/config -size +1c -type f`; do
		mkdir -p "$pkgdir/usr/src/linux-$_kernver/$(dirname $config)"
		cp -a $config "$pkgdir/usr/src/linux-$_kernver/$(dirname $config)"
	done

	# add headers
	for header in `find -size +1c -name '*.h'`; do
		mkdir -p "$pkgdir/usr/src/linux-$_kernver/$(dirname $header)"
		cp -a $header "$pkgdir/usr/src/linux-$_kernver/$(dirname $header)"
	done

	# copy in Kconfig files
	for i in `find . -name "Kconfig*"`; do
		mkdir -p "$pkgdir/usr/src/linux-$_kernver/$(echo $i | sed 's|/Kconfig.*||')"
		cp $i "$pkgdir/usr/src/linux-$_kernver/$i"
	done

	# strip scripts directory
	find "$pkgdir/usr/src/linux-$_kernver/scripts" -type f -perm -u+w 2>/dev/null | while read binary ; do
		case "$(file -bi "$binary")" in
			*application/x-sharedlib*) # Libraries (.so)
				/usr/bin/strip $STRIP_SHARED "$binary"
			;;
			*application/x-archive*) # Libraries (.a)
				/usr/bin/strip $STRIP_STATIC "$binary"
			;;
			*application/x-executable*) # Binaries
				/usr/bin/strip $STRIP_BINARIES "$binary"
			;;
		esac
	done

	chown -R root:root "$pkgdir/usr/src/linux-$_kernver"
	find "$pkgdir/usr/src/linux-$_kernver" -type d -exec chmod 755 {} \;
	# remove unneeded architectures
	rm -rf "$pkgdir/usr/src/linux-$_kernver/arch"/{alpha,arm,arm26,avr32,blackfin,cris,frv,h8300,ia64,m32r,m68k,m68knommu,mips,microblaze,mn10300,parisc,powerpc,ppc,s390,score,sh,sh64,sparc,sparc64,tile,um,v850,xtensa,arm64,c6x,hexagon,openrisc,unicore32}
}
