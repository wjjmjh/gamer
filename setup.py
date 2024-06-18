from setuptools import find_packages, setup

PACKAGE_DIR = "."

setup(
    name="gamer",
    packages=find_packages(),
    package_dir={"": PACKAGE_DIR},
    install_requires=[],
    extras_require={"dev": ["pytest", "tox", "black", "isort"]},
)
