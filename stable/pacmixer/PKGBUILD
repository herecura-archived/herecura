# Maintainer: Karol "Kenji Takahashi" Wozniak <wozniakk@gmail.com>

pkgname=pacmixer
pkgver=0.6.1
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
    'ninja'
)
source=("$pkgname-$pkgver.tar.gz::https://github.com/KenjiTakahashi/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('2c972d59eba1cb3b9ea5c0a481c9ac17b00643b90ac8a3d0c7d6be6e1a0ce268')

build() {
    cd "$pkgname-$pkgver"
    ./mk
}

package() {
    cd "$pkgname-$pkgver"
    DESTDIR="$pkgdir" PREFIX="/usr" ./mk install
}

