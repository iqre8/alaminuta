import apt
import sys
def remove(pkg_name):
    cache = apt.cache.Cache()
    cache.open()
    pkg = cache[pkg_name]
    cache.update()
    pkg.mark_delete(True, purge=True)
    resolver = apt.cache.ProblemResolver(cache)

    if pkg.is_installed is False:
        print (pkg_name + " not installed so not removed")
    else:
        for pkg in cache.get_changes():
            if pkg.mark_delete:
                print(pkg_name + " is installed and will be removed")
                resolver.remove(pkg)
    try:
        cache.commit()
        cache.close()
    except Exception as arg:
        sys.stderr.write("ERROR REMOVING PACKAGE [{err}]".format(err=str(arg)))
