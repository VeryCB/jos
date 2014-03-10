from setuptools import setup

from jos import __version__


with open('README.rst') as long_description_file:
    long_description = long_description_file.read()


setup(
    name='jos',
    version=__version__,
    url='https://github.com/verycb/jos',
    author='VeryCB',
    author_email='imcaibin@gmail.com',
    description='Jingdong API Client',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        "requests >= 1.0",
    ],
)
