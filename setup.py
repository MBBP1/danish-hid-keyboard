from setuptools import setup, find_packages

setup(
    name="danish-hid-keyboard",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.6",
    author="Mikkel B. Bentsen-Petersen",
    description="BadUSB bibliotek for dansk keyboard layout til Raspberry Pi",
    url="https://github.com/MBBP1/danish-hid-keyboard",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
