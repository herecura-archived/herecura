# Maintainer: Det <nimetonmaili at gmail a-dot com>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Stable%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome
pkgver=43.0.2357.124
pkgrel=1
pkgdesc="An attempt at creating a safer, faster, and more stable browser (Stable Channel)"
arch=('i686' 'x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=('alsa-lib' 'desktop-file-utils' 'flac' 'gconf' 'gtk2' 'harfbuzz' 'harfbuzz-icu' 'hicolor-icon-theme'
         'icu' 'libpng' 'libxss' 'libxtst' 'nss' 'opus' 'snappy' 'speech-dispatcher' 'ttf-font' 'xdg-utils')
optdepends=('kdebase-kdialog: needed for file dialogs in KDE'
            'ttf-google-fonts-git')
provides=("google-chrome=$pkgver")
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=stable
_arch=amd64
[[ $CARCH = i686 ]] && _arch=i386
source=(
	"google-chrome-${_channel}_${pkgver}_i386.deb::http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${pkgver}-1_i386.deb"
	"google-chrome-${_channel}_${pkgver}_amd64.deb::http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${pkgver}-1_amd64.deb"
	'http://www.google.com/chrome/intl/en/eula_text.html'
)
noextract=(
	"google-chrome-${_channel}_${pkgver}_i386.deb"
	"google-chrome-${_channel}_${pkgver}_amd64.deb"
)

prepare() {
	ar x "google-chrome-${_channel}_${pkgver}_${_arch}.deb"
}

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"

	# Icons
	for i in 16 22 24 32 48 64 128 256; do
		install -Dm644 "$pkgdir"/opt/google/chrome/product_logo_$i.png \
			"$pkgdir"/usr/share/icons/hicolor/${i}x$i/apps/google-chrome.png
	done

	# Man page
	gzip "$pkgdir"/usr/share/man/man1/google-chrome.1

	# License
	install -Dm644 eula_text.html "$pkgdir"/usr/share/licenses/google-chrome/eula_text.html

	# fix chrome to use libudev.so.1
	sed -e 's/libudev.so.0/libudev.so.1/g' \
		-i "$pkgdir/opt/google/chrome/chrome"

	_name=$(echo ${source/_*} | sed 's/.*/\u&/')
	sed -i "/Exec=/i\StartupWMClass=$_name" "$pkgdir"/usr/share/applications/google-chrome.desktop

	sed -i 's/ "$@"/"$CHROMIUM_USER_FLAGS" "$@"/' "$pkgdir"/opt/google/chrome/google-chrome

	rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/opt/google/chrome/cron/
	rm "$pkgdir"/opt/google/chrome/product_logo_*.png
}

sha256sums=('f720f1a98f2d659e8b718e9ad4ae03624f5e2ca27e031b41fc38f7181475c296'
            '59fe3f552bda115ea32dec6d26943d2fcd234ab5c96f781fe6f527e1d87dd174'
            '4242ecd421c56d47e56f6384be5621fe4e7b772c11036a72145d0e580a0f464c')
