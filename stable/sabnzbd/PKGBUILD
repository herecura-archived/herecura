pkgname=sabnzbd
_pkgname=SABnzbd
pkgver=0.7.6
pkgrel=1
pkgdesc="A web-interface based binary newsgrabber with NZB file support"
url="http://www.sabnzbd.org"
arch=("any")
license=("GPL")
depends=("curl" "par2cmdline"
	"python2" "python2-cheetah" "python2-feedparser" "python2-pyopenssl" "python2-yenc"
	"sqlite" "unrar" "unzip")
optdepends=("xdg-utils: registration of .nzb files")
install="${pkgname}.install"
backup=("etc/conf.d/${pkgname}" "opt/${pkgname}/${pkgname}.ini" "etc/conf.d/${pkgname}_systemd")
source=("http://downloads.sourceforge.net/sabnzbdplus/${_pkgname}-${pkgver}-src.tar.gz"
	"${pkgname}" "${pkgname}.confd" "${pkgname}.init" "${pkgname}.desktop"
	"addnzb.sh" "nzb-2.png" "sab2_64.png" "x-nzb.xml" "${pkgname}.service" "${pkgname}_systemd.confd" "${pkgname}.tmp")

package() {
	mkdir -p "${pkgdir}/opt/${pkgname}"
	touch "${pkgdir}/opt/${pkgname}/${pkgname}.ini"
	cp -rv "${srcdir}/${_pkgname}-${pkgver}/"* "${pkgdir}/opt/${pkgname}"

	# Fix for issues with Python 3
	find "${pkgdir}/opt/${pkgname}" -type f -exec sed -i 's/python/python2/g' {} \;
	find "${pkgdir}/opt/${pkgname}" -type d -exec chmod 755 {} \;
	find "${pkgdir}/opt/${pkgname}" -type f -exec chmod 644 {} \;
	chmod 755 "${pkgdir}/opt/${pkgname}/${_pkgname}.py"
	chmod 755 "${pkgdir}/opt/${pkgname}/Sample-PostProc.sh"

	install -Dm755 "${srcdir}/${pkgname}"       "${pkgdir}/usr/bin/${pkgname}"
	install -Dm755 "${srcdir}/${pkgname}.init"  "${pkgdir}/etc/rc.d/${pkgname}"
	install -Dm644 "${srcdir}/${pkgname}.confd" "${pkgdir}/etc/conf.d/${pkgname}"
	install -Dm644 "${srcdir}/${pkgname}_systemd.confd" "${pkgdir}/etc/conf.d/${pkgname}_systemd"
	install -Dm644 "${srcdir}/${pkgname}.tmp" "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
	install -Dm644 "${srcdir}/${pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
	install -Dm755 "${srcdir}/${pkgname}.desktop" \
		"${pkgdir}/usr/share/applications/${pkgname}.desktop"
	install -Dm755 "${srcdir}/addnzb.sh"    "${pkgdir}/opt/${pkgname}/addnzb.sh"
	install -Dm644 "${srcdir}/nzb-2.png"    "${pkgdir}/opt/${pkgname}/nzb-2.png"
	install -Dm644 "${srcdir}/sab2_64.png"  "${pkgdir}/opt/${pkgname}/sab2_64.png"
	install -Dm770 "${srcdir}/x-nzb.xml"    "${pkgdir}/opt/${pkgname}/x-nzb.xml"
}

sha256sums=('e2b3cd5c571b7bb4413693a178669b2a7fcb1b5c707b5228a818fc4c9b0ee6b8'
            '82630edfc767a383843ffaae9d716e99010dad9e93bdee08d541faa74e694a65'
            '7027b48f0051dcba1622166de0fb8c6f972f87e4b0f13de7785381d7bf624fa3'
            'bf74d29870a062f277a9126254019291352eada34053f74ea4d0b36d39f1b596'
            '6214a92f775888133a8f87ec69e4d0d2ecc9fafbe61387778767000e4db3ea8f'
            'baea3351a40551a63b90b4a4c32719d4c27b5fff596e74e4a91f289964960eb6'
            '7fec4494a04ffd6a94644c8ef499ec1c92998a613b1fde5c3a46f38c53dfbc43'
            '099d625d6efc9e69e7c6a2833221928fb19e9e356e3aa8341c36ffdc281e567d'
            'f53261d7578c67fb9fd6a639df94cd53604bcf37b9b03a926cb03e5214b496fe'
            '6ab902bd7e958d0daedad90807f67bdc6696143f6e01c2c17acc4c52027a6e2e'
            '3fc91a1e9fd3a099dfc2477f025c0c356fa8dccc575c206251b6cdb2e60c8dc1'
            'e28b746d200d70c34316bcc6c322f613b08d60a530348bfcaac9a73932618e35')
