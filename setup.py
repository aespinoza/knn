import os
import sys
import setuptools
from setuptools import setup

import knn

THIS_DIR = os.path.join(os.path.dirname(__file__))
with open(os.path.join(THIS_DIR, "requirements.txt"), "rb") as f:
    REQUIREMENTS = f.read().decode().split("\n")

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 8)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("Unsupported Python version")
    sys.exit(1)

setup(
    name="knn",
    version=knn.__version__,
    author="Alex Espinoza",
    author_email="aespinoza@structum.net",
    maintainer="Alex Espinoza",
    maintainer_email="aespinoza@structum.net",
    url="http://structum.io",
    description="KNN Learning Tool",
    long_description="K-Nearest Neighbor Learning Tool",
    license="Proprietary",
    packages=setuptools.find_packages(),
    install_requirements=REQUIREMENTS,
    platforms="Cross Platform",
    include_package_data=True,
    classifiers=[
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3"
    ],
)
