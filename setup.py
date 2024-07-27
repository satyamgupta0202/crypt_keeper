import setuptools


setuptools.setup(
    name="crypt_keeper",
    version="1.0.0",
    author="Satyam Gupta",
    author_email="satyamguptaece@gmail.com",
    packages=['crypt_keeper'],
    description="Package to encrypt and decrypt PII data using AES-128-CBC",
    url="https://github.com/Capri-Global-Capital-Ltd/core-encryption",
    license='unilicense',
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[
        'cryptography>=3.2',
        'pycryptodome>=3.10.1',
        'boto3>=1.15.0',
        'botocore>=1.12.201'
    ]
)