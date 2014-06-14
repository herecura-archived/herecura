# vim:set ft=sh:
# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >
# thx for the original vim pkg:
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: tobias [ tobias at archlinux org ]
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgbase=vim
pkgname=('vim-tiny' 'vim-cli' 'vim-gvim-gtk' 'vim-gvim-qt' 'vim-rt' 'vim-gvim-common')
_basever=7.4
_patchlevel=325
if [ "$_patchlevel" = "0" ]; then
	pkgver=${_basever}
else
	pkgver=${_basever}.${_patchlevel}
fi
__hgrev=v${pkgver//./-}
pkgrel=1
_versiondir=vim${_basever/./}
arch=('i686' 'x86_64')
license=('custom:vim')
url="http://www.vim.org"
makedepends=('gpm' 'perl' 'python2' 'python' 'lua' 'desktop-file-utils' 'gtk2' 'gettext' 'pkgconfig' 'sed' 'mercurial' 'qt4' 'ruby')
options=()
source=(
	"hg+https://code.google.com/p/vim/#tag=$__hgrev"
	'vimrc'
	'peaksea.vim'
	'gvim.desktop'
	'license.txt'
	'vim-qt-src.patch'
	'qt-icons.tar.gz'
	'qvim.desktop'
	'qvim.png'
)
sha256sums=(
	'SKIP'
	'868486500e70b4b45618cdae32fdb3b228baf3995e9ccce5e86bf54780431056'
	'1cbb92f80c981a9618bc50a626e2713435b7014cac842e664d0b3027f86bd209'
	'5f2d65e755424f688b990b20bce6bd84718b9d5f7944a5332b5dee72f09493f7'
	'bb4744930a0030085d382356e9fdd4f2049b6298147aee2470c7fca7ec82fd55'
	'0679566d70ef72d39e28af01e8d51cd7e9ba46c5c4e6a1a752054a804ab49b01'
	'b3fbdf437c75ffbb69cd8edbdf9ccf78522cbfdbce55d3cbb464c1bc707b85cf'
	'e61684f12ec23944903e37deb9d902a072ffa71d7c00fedea32c1176d84dc9bd'
	'c530f9d5dc6beb2cfa9e4e60dc8f74e1a26694d9f090f7ab0d40f8e963cfb280'
)

__hgroot='https://code.google.com/p/vim/'
__hgrepo='vim'
__hgbranch='default'

prepare() {
	# remove old build dirs if exist
	[ -d vim-build ] && rm -rf vim-build
	[ -d vim-build-tn ] && rm -rf vim-build-tn
	[ -d gvim-build-gtk ] && rm -rf gvim-build-gtk
	[ -d gvim-build-qt ] && rm -rf gvim-build-qt

	cp -a ${pkgbase} vim-build
	(
		cd vim-build && rm -rf ./.hg*
	)

	# define the place for the global (g)vimrc file (set to /etc/vimrc)
	sed -i 's|^.*\(#define SYS_.*VIMRC_FILE.*"\) .*$|\1|' \
		vim-build/src/feature.h
	sed -i 's|^.*\(#define VIMRC_FILE.*"\) .*$|\1|' \
		vim-build/src/feature.h

	msg2 'Building...'

	cp -a vim-build vim-build-tn
	cp -a vim-build gvim-build-gtk
	cp -a vim-build gvim-build-qt
}

build() {
	msg2 'Building vim-tiny'
	cd ${srcdir}/vim-build-tn
	(cd src && autoconf)
	./configure --prefix=/usr --localstatedir=/var/lib/vim \
		--mandir=/usr/share/man --with-compiledby=BlackEagle \
		--with-features=tiny --disable-gpm --enable-acl --with-x=no \
		--disable-gui --enable-multibyte --disable-cscope \
		--disable-netbeans --disable-perlinterp --disable-pythoninterp \
		--disable-rubyinterp --enable-luainterp=no
	make

	msg2 'Building vim-cli'
	cd ${srcdir}/vim-build
	(cd src && autoconf)
	./configure --prefix=/usr --localstatedir=/var/lib/vim \
		--mandir=/usr/share/man --with-compiledby=BlackEagle \
		--with-features=huge --enable-gpm --enable-acl --with-x=yes \
		--disable-gui --enable-multibyte --enable-cscope \
		--disable-netbeans --enable-perlinterp=dynamic \
		--enable-pythoninterp=dynamic --enable-python3interp=dynamic \
		--enable-rubyinterp=dynamic --enable-luainterp=dynamic
		#--disable-rubyinterp --enable-luainterp=dynamic
	make

	msg2 'Building vim-gvim-gtk'
	cd ${srcdir}/gvim-build-gtk
	(cd src && autoconf)
	./configure --prefix=/usr --localstatedir=/var/lib/vim \
		--mandir=/usr/share/man --with-compiledby=BlackEagle \
		--with-features=huge --enable-gpm --enable-acl --with-x=yes \
		--enable-gui=gtk2 --enable-multibyte --enable-cscope \
		--enable-netbeans  --enable-perlinterp=dynamic \
		--enable-pythoninterp=dynamic --enable-python3interp=dynamic \
		--enable-rubyinterp=dynamic --enable-luainterp=dynamic
		#--disable-rubyinterp --enable-luainterp=dynamic
	make

	msg2 'Building vim-gvim-qt'
	cd ${srcdir}/gvim-build-qt
	(cd src && autoconf)
	patch -Np1 -i ${srcdir}/vim-qt-src.patch
	(cd src/qt && tar -zxf ${srcdir}/qt-icons.tar.gz)
	export PATH=$PATH:/usr/lib/qt4/bin
	./configure --prefix=/usr --localstatedir=/var/lib/vim \
		--mandir=/usr/share/man --with-compiledby=BlackEagle \
		--with-features=huge --enable-gpm --enable-acl --with-x=yes \
		--enable-gui=qt --enable-multibyte --enable-cscope \
		--enable-netbeans  --enable-perlinterp=dynamic \
		--enable-pythoninterp=dynamic --enable-python3interp=dynamic \
		--enable-rubyinterp=dynamic --enable-luainterp=dynamic
		#--disable-rubyinterp --enable-luainterp=dynamic
	make
}

package_vim-tiny() {
	pkgdesc='Vi Improved, tiny edition'
	conflicts=('vi' 'vim')
	provides=('vim')

	cd ${srcdir}/vim-build-tn
	make -j1 VIMRCLOC=/etc DESTDIR=${pkgdir} install

	# Runtime not needed
	rm -r ${pkgdir}/usr/share/vim

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-tiny
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-tiny/license.txt
}

package_vim-cli() {
	pkgdesc='Vi Improved, cli'
	depends=("vim-rt=${pkgver}-${pkgrel}" 'gpm' 'libxt')
	optdepends=(
		'perl: vim perl binding'
		'python2: vim python2 binding'
		'python: vim python3 binding'
		'lua: vim lua binding'
		'ruby: vim ruby binding'
	)
	conflicts=('vi' 'vim')
	provides=('vim')

	cd ${srcdir}/vim-build
	make -j1 VIMRCLOC=/etc DESTDIR=${pkgdir} install

	# remove evim manpages
	rm -f ${pkgdir}/usr/share/man/*{,/*}/evim*

	# Runtime provided by runtime package
	rm -r ${pkgdir}/usr/share/vim

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-cli
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-cli/license.txt
}

package_vim-gvim-gtk() {
	pkgdesc='Vi Improved, gtk gui'
	depends=('vim-cli' 'vim-gvim-common' 'desktop-file-utils' 'gtk2')
	provides=('gvim')
	install=gvim.install

	cd ${srcdir}/gvim-build-gtk
	make -j1 VIMRCLOC=/etc DESTDIR=${pkgdir} install

	# move vim to gvim
	rm -f ${pkgdir}/usr/bin/gvim
	mv ${pkgdir}/usr/bin/{vim,gvim}
	# remove files provided by vim-cli
	rm -f ${pkgdir}/usr/bin/{vimtutor,xxd,rview,rvim,view,vimdiff,ex}
	rm -f ${pkgdir}/usr/share/man/*{,/*}/{vim*,vimtutor*,xxd*,rview*,rvim*,view*,vimdiff*,ex*}
	# recreate gvim symlinks
	(
	cd ${pkgdir}/usr/bin
	for link in eview evim gview gvimdiff rgview rgvim; do
		rm -f ${link}
		ln -s gvim ${link}
	done
	)

	# Runtime provided by runtime package
	rm -r ${pkgdir}/usr/share/vim

	# Move the man pages for common packaging
	mv ${pkgdir}/usr/share/man ${srcdir}/gvim-man-install

	# freedesktop links
	install -Dm644 ${srcdir}/gvim.desktop \
		${pkgdir}/usr/share/applications/gvim.desktop
	install -Dm644 runtime/vim48x48.png ${pkgdir}/usr/share/pixmaps/gvim.png

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-gvim-gtk
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-gvim-gtk/license.txt
}

package_vim-gvim-qt() {
	pkgdesc='Vi Improved, qt gui'
	depends=('vim-cli' 'vim-gvim-common' 'desktop-file-utils' 'qt4')
	provides=('gvim')
	install=gvim.install

	cd ${srcdir}/gvim-build-qt
	make -j1 VIMRCLOC=/etc DESTDIR=${pkgdir} install

	# move vim to gvim
	rm -f ${pkgdir}/usr/bin/gvim
	mv ${pkgdir}/usr/bin/{vim,qvim}
	# remove files provided by vim-cli
	rm -f ${pkgdir}/usr/bin/{vimtutor,xxd,rview,rvim,view,vimdiff,ex}
	rm -f ${pkgdir}/usr/share/man/*{,/*}/{vim*,vimtutor*,xxd*,rview*,rvim*,view*,vimdiff*,ex*}
	# move gvimtutor to qvimtutor
	mv ${pkgdir}/usr/bin/{gvimtutor,qvimtutor}
	# recreate gvim symlinks
	(
	cd ${pkgdir}/usr/bin
	for link in qview qvimdiff rqview rqvim; do
		rm -f ${link}
		ln -s qvim ${link}
	done
	)

	# Move the runtime for later packaging
	mv ${pkgdir}/usr/share/vim ${srcdir}/runtime-install

	# remove the man pages for common packaging
	rm -r ${pkgdir}/usr/share/man

	# freedesktop links
	install -Dm644 ${srcdir}/qvim.desktop \
		${pkgdir}/usr/share/applications/qvim.desktop
	install -Dm644 ${srcdir}/qvim.png ${pkgdir}/usr/share/pixmaps/qvim.png

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-gvim-qt
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-gvim-x11/license.txt
}

package_vim-rt() {
	pkgdesc='Runtime for vim and gvim'
	conflicts=('vim-runtime')
	provides=('vim-runtime')
	backup=('etc/vimrc')

	# Install the runtime split from gvim
	install -dm755 ${pkgdir}/usr/share
	mv ${srcdir}/runtime-install ${pkgdir}/usr/share/vim

	# fix FS#22661 add rgb.txt
	install -Dm644 ${srcdir}/vim/runtime/rgb.txt \
		${pkgdir}/usr/share/vim/${_versiondir}/rgb.txt

	# fix FS#17216
	sed -i 's|messages,/var|messages,/var/log/messages.log,/var|' \
		${pkgdir}/usr/share/vim/${_versiondir}/filetype.vim

	# patch filetype.vim for better handling of pacman related files
	sed -i "s/rpmsave/pacsave/;s/rpmnew/pacnew/;s/,\*\.ebuild/\0,PKGBUILD*,*.install/" \
		${pkgdir}/usr/share/vim/${_versiondir}/filetype.vim
	sed -i "/find the end/,+3{s/changelog_date_entry_search/changelog_date_end_entry_search/}" \
		${pkgdir}/usr/share/vim/${_versiondir}/ftplugin/changelog.vim

	# rc files
	#install -dm755 ${pkgdir}/etc/vim
	install -Dm644 ${srcdir}/vimrc ${pkgdir}/etc/vimrc
	install -dm755 ${pkgdir}/usr/share/vim/vimfiles/colors
	install -Dm644 ${srcdir}/peaksea.vim \
		${pkgdir}/usr/share/vim/vimfiles/colors/peaksea.vim

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-rt
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-rt/license.txt
}

package_vim-gvim-common() {
	pkgdesc='common files for gvim/qvim'

	# Install the common split from gvim/qvim
	install -dm755 ${pkgdir}/usr/share
	mv ${srcdir}/gvim-man-install ${pkgdir}/usr/share/man

	# license
	install -dm755 ${pkgdir}/usr/share/licenses/vim-gvim-common
	install -Dm644 ${srcdir}/license.txt \
		${pkgdir}/usr/share/licenses/vim-gvim-common/license.txt
}

