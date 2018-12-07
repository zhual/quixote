import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyquixote",
    version="0.0.1",
    author="ZIJIAN JIANG",
    author_email="jiangzijian77@gmail.com",
    description="A minimal dataflow based computational graph library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CallmeNezha/quixote",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "typing>=3.6.6",
        "setuptools>=39.0.1",
        "pip>=9.0.3",
        "PyYAML>=3.13"
    ]
)