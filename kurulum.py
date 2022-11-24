import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamtape-api", 
    version="1.0",
    description="Python icin Streamtape api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/whomiri/streamtape-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
