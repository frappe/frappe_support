from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in support/__init__.py
from support import __version__ as version

setup(
	name="support",
	version=version,
	description="A simple support app",
	author="developers@frappe.io",
	author_email="developers@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
