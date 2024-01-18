import subprocess
import sys

def is_package_installed(package_name):
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = installed_packages.decode('utf-8').split('\n')
    return any(package_name in package for package in installed_packages)

def install_package(package_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
def CheckIfSeliniumIsInstalled():
# Check if Selenium is installed
 if not is_package_installed('selenium'):
    print("Selenium nije instaliran. Insaliram...")
    install_package('selenium')
    print("Selenium uspesno instaliran.")
 else:
    print("Selenium je vec instaliran.")