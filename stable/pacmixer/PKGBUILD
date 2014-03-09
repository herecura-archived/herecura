# Maintainer: Karol "Kenji Takahashi" Wozniak <wozniakk@gmail.com>

pkgname=pacmixer
pkgver=0.4.1
pkgrel=1
pkgdesc="alsamixer alike for PulseAudio."
arch=('i686' 'x86_64')
url="https://github.com/KenjiTakahashi/pacmixer"
license=('GPL3')
depends=(
    'ncurses'
    'libpulse'
    'gnustep-base'
)
makedepends=(
    'gcc-objc'
)
provides=('pacmixer')
source=("$pkgname-$pkgver.tar.gz::https://github.com/KenjiTakahashi/$pkgname/archive/$pkgver.tar.gz")

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR=$pkgdir PREFIX="/usr" install
}

sha256sums=('f1349b81a8fe342956182ae8f8febc9f8c55260a8a475a268ccd26d7fb75e3f7')
