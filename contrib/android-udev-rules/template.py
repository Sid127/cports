pkgname = "android-udev-rules"
pkgver = "20240221"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "625b43fd1df210cbb7a7508d9d16680b67deac1f5052fee0bad9ce660f17db49"
options = ["!splitudev"]


def do_install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
