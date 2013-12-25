# Maintainer: Karol "Kenji Takahashi" Wozniak <wozniakk@gmail.com>

pkgname=pacmixer
pkgver=0.4
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

sha256sums=('7b29e6194fa67601338292a77bcac8000b800a0bccd7666b520824f3d90c4dfe')
