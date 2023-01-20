"""
To build distribution: python setup.py sdist bdist_wheel --universal
"""
import setuptools

pkg = "onex_dataflowapi"
version = "0.0.48"

setuptools.setup(
    name=pkg,
    version=version,
    description="The Open Network Experiments (ONEx) Python Package",
    long_description="A long description",
    long_description_content_type="text/markdown",
    url="https://github.com/open-network-experiments/models",
    author="Open Network Experiments (ONEx)",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="onex open network experiments testing automation",
    include_package_data=True,
    packages=[pkg],
    python_requires=">=2.7, <4",
    install_requires=[
        "pyyaml",
    ]
)