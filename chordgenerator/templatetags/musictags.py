#!/usr/bin/python 
#-*- coding: UTF-8 -*-
# File:musictags.py 
# Goal - to provide a nice template tag to represent tables of chords.

from musictheory.musutility import seqtostr;
from musictheory.temperament import un_unicode_accdtls;
from musictheory.chordgenerator import int_to_roman, scale_chords;
from django import template;
from django.utils.safestring import mark_safe

register = template.Library();

# Note: this is a copy of chordgentable from musictheory. This method should belong here.

def chordgentableneu(scales):
    """ Generates a table representation of a series of scales,
        represented by a scale_chords instance. """
    startrow  = "<tr>\n";
    endrow = "</tr>\n";
    thestring = u"";
    for scale in scales:
        thestring += "<h2>%s</h2>\n" % (scale.key + " " +scale.full_name);
        thestring += ("<table id=\"%s\" class=\"chordtable table-bordered table-striped\">\n" % 
            (scale.key + ""));
        thestring += "<caption>%s</caption>\n" % (scale.key + " " + scale.full_name +
            ": " + seqtostr(scale.full_notes));
        thestring += "<thead>\n" + startrow + "<th class=\"text-center\">Chord Types</th>\n";
        for q in range(7):
            thestring += "<th class=\"text-center\">%s</th>\n" % str(int_to_roman(q+1));
        thestring += endrow + "</thead>\n<tbody>\n";

        for i in scale.rows:
            thestring += startrow;    
            thestring += "<td>%s</td>\n" % i.chord_type;
            for j in i.notes:
                if not j.chordname_1:
                    thestring += ("<td><p>%s<br />" % (unicode(j.chordname_1)));
                    thestring += ("<i>%s</i><br />" % (unicode(j.chordname_2)));
                else:
                    thestring += ("<td><p>%s<br />" % (j.notes[0]+" "+unicode(j.chordname_1)));
                    thestring += ("<i>%s</i><br />" % (j.notes[0]+unicode(j.chordname_2)));
                    
                thestring += ("<b>%s</b></p></td>" % seqtostr(j.notes));                
            thestring += endrow;    
        thestring += "\n</tbody>\n</table>\n";    
    return thestring;




@register.filter(name="chordtabletag")
def chordtabletag(value, arg = False):
    ''' Takes an argument (value) that is assumed to be of type scale_chords.
    The function is really a wrapper around chordgentable. The arg argument
    indicates whether it is ASCII-only (True) or Unicode (False).
    '''
    try:
        
# Any exception - any at all - returns an empty string.

        output = chordgentableneu([value]);
        if arg:
            output = un_unicode_accdtls(output);
        return mark_safe(output);

# And if it all turns to shit...

    except:
        return "";
chordtabletag.is_safe = False








