# Maintainer: Det <nimetonmaili at gmail a-dot com>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Stable%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome
pkgver=41.0.2272.89
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

sha256sums=('6407a5328283a101a248c92632964e1ddb85900cb54bde23776486ab237859a7'
            'db6dda9c789cd6e5f96f9585179d56cbdff407505ce1d0d691514bbd9e7368b9'
            '4242ecd421c56d47e56f6384be5621fe4e7b772c11036a72145d0e580a0f464c')
