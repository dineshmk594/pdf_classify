"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Dineshkumar",
    author_email="dineshmk594@gmail.com",
    name='pdf_classify',
    license="MIT",
    description='pdf_classify is a python package used to classify of digital and scanned pdf.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/dineshmk594/pdf_classify',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['PyPDF2'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
