import json
from setuptools import setup, find_packages

with open("version.json") as versionf:
    versionJSON = json.load(versionf)

with open("requirements.txt", "r") as require:
    requirements = require.read()

setup(
    name='hacky-vonslacky',
    version=versionJSON["version"],
    install_requires=requirements,
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
