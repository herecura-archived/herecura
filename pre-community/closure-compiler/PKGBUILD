# $Id$
# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Bram Schoenmakers <me@bramschoenmakers.nl>
pkgname=closure-compiler
pkgver=20141120
pkgrel=1
pkgdesc="Performs checking, instrumentation and optimizations on Javascript code."
arch=('any')
url="https://developers.google.com/closure/compiler/"
license=('APACHE')
depends=('java-runtime')
makedepends=('apache-ant')
source=("$pkgname-$pkgver.tar.gz::https://github.com/google/$pkgname/archive/v$pkgver.tar.gz")

build() {
	cd "$pkgname-$pkgver"

	ant jar
}

check() {
	cd "$pkgname-$pkgver"

	ant test
}

package() {
	cd "$pkgname-$pkgver"

	install -m755 -D build/compiler.jar "$pkgdir/usr/share/java/closure-compiler/closure-compiler.jar"
	mkdir $pkgdir/usr/bin
	echo '#!/bin/sh
	"$JAVA_HOME/bin/java" -jar /usr/share/java/closure-compiler/closure-compiler.jar $@' > "$pkgdir/usr/bin/closure"
	chmod +x "$pkgdir/usr/bin/closure"
}

sha256sums=('46ef35d1d53ccf02b09aed061b516ae07d286ae623dbec94c40064747bdceabf')
