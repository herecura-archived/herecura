# Maintainer: Karol "Kenji Takahashi" Wozniak <wozniakk@gmail.com>

pkgname=pacmixer
pkgver=0.5
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

sha256sums=('4c86c401201369b0be4a9edf25be682debab198b5599ed78c9fc8d9af2cea4f3')
