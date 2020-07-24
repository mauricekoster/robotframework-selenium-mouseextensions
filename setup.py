from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="robotframework-selenium-mouseextensions",
    version="0.1-2",
    packages=["SeleniumMouseExtensions"],
    install_requires=["robotframework-seleniumlibrary"],

    author="Maurice Koster",
    author_email="maurice@mauricekoster.com",
    description="Extra mouse actions missing from the standard SeleniumLibrary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="robotframework selenium",
    url="https://github.com/mauricekoster/robotframework-selenium-mouseextensions/",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
