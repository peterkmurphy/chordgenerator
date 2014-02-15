===============
Chord Generator
===============

About
-----

**Chord Generator** is a Django application for enumerating all possible chords
in a selected scale. In particular, **Chord Generator** will show what the chord
is for a given *chord type* and *position*, if such a chord exists. A demonstration
is available `here <http://www.pkmurphy.com.au/chordgenerator/>`_.

Installation and Dependencies
-----------------------------

You can get **Chord Generator** from PyPI through the command:

    pip install chordgenerator

Once installed, just add "chordgenerator" to your INSTALLED_APPS list in settings.py,
and add the desired URL in one of the urls.py files.

Apart from `Django <https://www.djangoproject.com/>`_, the app depends on `musictheory
<https://pypi.python.org/pypi/musictheory/>`_. This package - also made by myself - 
is the guts of the application, and can be used outside of Django. It contains classes
for musical temperaments, scales and chords.

The HTML template file used to generate HTML has been redesigned to work with the 
`Mezzanine <http://mezzanine.jupo.org/>`_ CMS. The redesign removed any explicit 
references to particular stylesheets found with earlier versions. Feel free to 
customise: the app is released under a 3 clause BSD license. If you wish to do any 
changes to the app, pop over to the `GitHub repository <https://github.com/peterkmurphy/chordgenerator>`_. 
(There is also a `Github repository for musictheory <https://github.com/peterkmurphy/musictheory>`_.)

Versions
--------

* 0.1 (May 1st 2011) - Initial release. Took code and made setup script.

* 0.2 (May 11th 2011) - Remove bugs.

* 0.3 (June 6th 2011) - Add license information. Add more scales.

* 0.4 (June 2nd 2013) - Try to make a half-decent PyPI package.

* 0.5 (January 30th 2014) - Updated to be compatible with Django 1.6 and Mezzanine 3.0.

* 0.6 (February 15th 2014) - Added more styling to be compatible with Bootstrap. More history described.

Copyright
---------

The **Chord Generator** app is copyright (c) 2008-2014 
`Peter Murphy <http://www.pkmurphy.com.au/>`_ 
<peterkmurphy@gmail.com>.




