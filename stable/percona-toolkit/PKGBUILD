# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: Felix Hanley <felix@seconddrawer.com.au>
pkgname=percona-toolkit
pkgver=2.2.7
pkgrel=1
pkgdesc="A collection of advanced command-line tools to perform a variety of MySQL and system tasks."
url="http://www.percona.com/software/percona-toolkit/"
arch=('any')
license=('GPLv2')
depends=('perl-dbi' 'perl-dbd-mysql' 'perl-time-hires' 'perl-term-readkey')
makedepends=('perl')
source=("http://www.percona.com/redir/downloads/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.gz")
md5sums=('7514af32e0edff70c4934da2e5e36303')

prepare() {
    export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
    perl Makefile.PL PREFIX=/usr
    make
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
    make install INSTALLDIRS=vendor DESTDIR="$pkgdir"
}

# vim: set ts=4 sw=4 tw=0 ft=sh et :
