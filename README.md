# Dependency Confusion

## What Dependency Confusion Attacks Are
Dependency confusion is a supply chain exploit that exploits
certain package managers to inject malicious code. 

Many package managers check public registries for a 
package before private registries. Accordingly, if a package exists in a private registry, 
a malicious actor can register a package of the same name within the public registry. 

If the version number of a public package is greater than that of a private package of the same name,
the package manager (in this case PIP), would install and update the package from the public registry.
Obviously, this is bad.

This was discovered by Alex Birsan, his medium blog post is worth reading to understand this attack: 
https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610

## Upload package with Twine

Install twine with pip or pip3
```shell
pip install twine
```

Setup file must look something like this, setup function is essential, any malicious code should be executed after 
setup function has been called.
```python3
from setuptools import setup, find_packages

setup(
    name = "package_name-2.0.3",
    version = "2.0.3",
    packages = find_packages()
)
```

Run setup.py
```shell
python3 setup.py sdist
```

Upload
```shell
twine upload dist/*
```

## Mitigations
### Using a single feed: Python Package Index, NuGetGallery, and Maven

### Python Package Index
Use the index-url option in pip’s configuration file or CLI to
specify the feed, overriding the default. Avoid the extra-index-url option.

https://pip.pypa.io/en/stable/user_guide/#config-file

Pip’s hash-checking mode ensures that the downloaded file matches a
known SHA256 hash stored in your project. Generating the hashes requires [pip-compile](https://pypi.org/project/pip-tools/) . 

https://aka.ms/AAb1qo5

### NuGetGallery
```shell
-i, --index-url <url>       Base URL of Python Package Index (default https://my.local.mirror.com/simple)
```
Ensure your nuget.config packageSources section starts with a ```<clear
/>``` entry to remove any inherited configuration, and use a single ```<add />``` entry for your
private feed.

https://learn.microsoft.com/en-us/nuget/reference/nuget-config-file

### Maven
Configure a single mirror that is ```<mirrorOf>*</mirrorOf>``` to direct all
requests through a single repository that performs its own redirection.

### NPM
Installing from a package.json file automatically updates the package-
lock.json file with versions and file hashes of packages. When package-lock.json is
included with your project, running the ```npm ci``` will replicate the install
using version pinning and integrity checking. Frees from manually pinning versions in the package.json file.
