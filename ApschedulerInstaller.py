import subprocess
import sys

def is_package_installed(package_name):
    """Check if a Python package is installed."""
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]
    return package_name.lower() in installed_packages

def install_package(package_name):
    """Install a Python package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

# Check and install setuptools if pkg_resources is missing
    
def PackageInstaller():
 try:
    import pkg_resources
 except ImportError:
    print("pkg_resources is missing. Installing setuptools...")
    install_package('setuptools')
    print("Setuptools installed successfully.")

# Check and install APScheduler
 if not is_package_installed('apscheduler'):
    print("APScheduler is not installed. Installing now...")
    install_package('apscheduler')
    print("APScheduler installed successfully.")
 else:
    print("APScheduler is already installed.")