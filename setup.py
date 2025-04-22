from setuptools import setup, find_packages

setup(
    name='PyNFe',
    version='0.9',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/cert/*.cer'],
    },
    install_requires=[
        "pyopenssl",
        "requests",
        "lxml",
        "signxml",
    ],
    zip_safe=False,
)
