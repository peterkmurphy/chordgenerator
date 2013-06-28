#!/usr/bin/python 
#-*- coding: UTF-8 -*-
# File:musictags.py 
# Goal - to provide a nice template tag to represent tables of chords.

from musictheory.temperament import un_unicode_accdtls;
from musictheory.chordgenerator import chordgentable, scale_chords;
from django import template;
from django.utils.safestring import mark_safe

register = template.Library();

@register.filter(name="chordtabletag")
def chordtabletag(value, arg = False):
    ''' Takes an argument (value) that is assumed to be of type scale_chords.
    The function is really a wrapper around chordgentable. The arg argument
    indicates whether it is ASCII-only (True) or Unicode (False).
    '''
    try:
        
# Any exception - any at all - returns an empty string.

        output = chordgentable([value]);
        if arg:
            output = un_unicode_accdtls(output);
        return mark_safe(output);

# And if it all turns to shit...

    except:
        return "";
chordtabletag.is_safe = False








