# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >
pkgname=wapiti
pkgver=2.2.1
pkgrel=2
pkgdesc="Wapiti is a vulnerability scanner for web applications."
url='http://wapiti.sourceforge.net/'
license=('GPL')
depends=('python2')
arch=('any')

source=("http://downloads.sourceforge.net/sourceforge/wapiti/$pkgname-$pkgver.tar.bz2")
sha256sums=('1ce7de9dd277c1ef2dde969cb0dfea61f551d5d08334fad4edbda08bf0724c09')

build() {
    mkdir -p $pkgdir/usr/share
    mkdir -p $pkgdir/usr/bin
    
    cp -r $srcdir/$pkgname-$pkgver $pkgdir/usr/share
    cd $pkgdir/usr/share/$pkgname-$pkgver
    
    cat > $pkgdir/usr/bin/$pkgname <<EOF
cd /usr/share/$pkgname-$pkgver/src/ && python2 wapiti.py \$*
EOF
    chmod +x $pkgdir/usr/bin/$pkgname
}
