#!/usr/bin/env python

from setuptools import setup

setup(name='chordgenerator',
    version='0.6',
    description='A Django app for enumerating chords in a scale.',
    author='Peter Murphy',
    author_email='peterkmurphy@gmail.com',
    url='http://pypi.python.org/pypi/chordgenerator/',
    packages=['chordgenerator', 'chordgenerator.templatetags'],
    package_data={
        'chordgenerator': [
            'templates/chordgenerator/*.html',
        ],
    },
    keywords = 'music scale chords Django',
    license='LICENSE.txt',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        'License :: OSI Approved :: BSD License',        
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',        
        'Topic :: Artistic Software',
        'Topic :: Education',
        'Topic :: Multimedia :: Sound/Audio',
        ],
    long_description=open('README.txt').read(),
    install_requires = ["Django >= 1.1.1", "musictheory >= 0.2"],
)
