import subprocess
import sys

def is_package_installed(package_name):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]
    return package_name.lower() in installed_packages

def install_package(package_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

# Check and install setuptools if pkg_resources is missing
    
def PackageInstaller():
 try:
    import pkg_resources
 except ImportError:
    print("pkg_resources nedostaj. Instaliram setuptools...")
    install_package('setuptools')
    print("Setuptools instalirani uspešno.")

# Check and install APScheduler
 if not is_package_installed('apscheduler'):
    print("APScheduler nije instaliran. Instaliram sada...")
    install_package('apscheduler')
    print("APScheduler uspešno instaliran.")
 else:
    print("APScheduler je već instaliran.")