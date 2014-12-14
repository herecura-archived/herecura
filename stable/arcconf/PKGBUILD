pkgname='arcconf'
_buildver='21062'
pkgver="1.06.$_buildver"
pkgrel=1
pkgdesc='Adaptec ARCCONF command line interface utility'
arch=('i686' 'x86_64')
url=('http://adaptec.com/')
license=('freeware')
depends=('bash')

source=("http://download.adaptec.com/raid/storage_manager/arcconf_v1_6_${_buildver}.zip")
sha256sums=('fb740cb308fe8290f32b7e68f8f5bec54f9784a7377086769f2e2ec23e402ed0')

package() {
  if [[ "$CARCH" == "x86_64" ]]; then
    install -Dm755 "$srcdir/linux_x64/cmdline/arcconf" "$pkgdir/usr/bin/arcconf"
  elif [[ "$CARCH" == "i686" ]]; then
    install -Dm755 "$srcdir/linux/cmdline/arcconf" "$pkgdir/usr/bin/arcconf"
  fi
}
