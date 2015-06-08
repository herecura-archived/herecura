# Maintainer: Karol "Kenji Takahashi" Wozniak <wozniakk@gmail.com>

pkgname=pacmixer
pkgver=0.6
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
sha256sums=('452c978b275da384653d3277c1d3ddf9650ce9cf6821cb3d5d29860cf139c2d7')

build() {
    cd "$pkgname-$pkgver"
    ./mk
}

package() {
    cd "$pkgname-$pkgver"
    DESTDIR="$pkgdir" PREFIX="/usr" ./mk install
}

