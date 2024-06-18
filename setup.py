# setup.py

from setuptools import setup, find_packages

setup(
    name="nas_file_access",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Your Name",
    author_email="khaangnguyeen@gmail.com",
    description="A package to access files on a NAS using only the path",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khengyun/nas_file_access",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
