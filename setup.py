import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pfreeze",
    version="0.1.0",
    author="Andres Bonilla",
    description="Pip freeze wrapper with prod/dev filter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[],
    classifiers=[
        "Development Status :: 3 - Alpha"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
    py_modules=["pfreeze"],
    package_dir={'': 'pfreeze'},
    install_requires=[],
)
