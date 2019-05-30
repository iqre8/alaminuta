import apt
import sys
def install(pkg_name):
    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print("{pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        pkg.mark_install()

        try:
            cache.commit()
        except Exception as arg:
            sys.stderr.write("ERROR WHILE INSTALLING PACKAGE [{0}]".format(arg))
