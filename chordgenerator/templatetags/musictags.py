#!/usr/bin/python 
#-*- coding: UTF-8 -*-
# File:musictags.py 
# Goal - to provide a nice template tag to represent tables of chords.

from musictheory.musutility import seqtostr;
from musictheory.temperament import un_unicode_accdtls, WestTemp;
from musictheory.chordgenerator import int_to_roman, scale_chords;
from django import template;
from django.utils.safestring import mark_safe

register = template.Library();

# PKM2014 - for each chord listed in the table, we want to get a starting note, and a 
# list of positions relative to it. For 9th, 11th and 13th chords, we need the position
# to be adjusted by 12. The reason is that the harmonies for 9th, 11th and 13th
# sound better with an extra octave.

def get_keyseq_notes_adjusted(temp, note_seq):
    ourseqnotes = temp.get_keyseq_notes(note_seq);
    ourseqnotenorm = temp.get_key_of_pos(temp.get_pos_of_key(ourseqnotes[0]))
    ourseqnotes[0] = ourseqnotenorm
    ourseqbase = ourseqnotes[1];
    ourseqlen = len(ourseqbase)
    snap = None
    for i in range(ourseqlen):
        if ((i < (ourseqlen - 1)) and (ourseqbase[i+1] < ourseqbase[i])):
            snap = i + 1;
            break;
    if not snap:
        return ourseqnotes
    else:
        ournewseq = ourseqbase;
        for i in range(ourseqlen):
            if i >= snap:
                ournewseq[i] = ournewseq[i] + temp.no_keys;
        return [ourseqnotes[0], ournewseq]


def getkeyseqid(keyseqnotes):
    """ Expressed as a id """
    ourreturn = keyseqnotes[0] + '-';
    ourlen = len(keyseqnotes[1]);
    for i, v in enumerate(keyseqnotes[1]):
        ourreturn += str(v);
        if i != ourlen - 1:
            ourreturn += '-';
    return ourreturn;

# Note: this is a copy of chordgentable from musictheory. This method should belong here.

def chordgentableneu(scales):
    """ Generates a table representation of a series of scales,
        represented by a scale_chords instance. """
    startrow  = "<tr>\n";
    endrow = "</tr>\n";
    thestring = "";
    for scale in scales:
        thestring += "<h2>%s</h2>\n" % (scale.key + " " +scale.full_name);
        thestring += ("<table id=\"%s\" class=\"chordtable table-bordered table-striped\">\n" % 
            (scale.key + ""));
        thestring += "<caption>%s</caption>\n" % (scale.key + " " + scale.full_name +
            ": " + seqtostr(scale.full_notes));
        thestring += "<thead>\n" + startrow + "<th class=\"text-center\">Chord Types</th>\n";
        
# PKM2014 - originally:       
        
#        for q in range(7):
#            thestring += "<th class=\"text-center\">%s</th>\n" % str(int_to_roman(q+1));
            
# Now
        basedone = False;    
        for i in scale.full_notes:
            ourseqnoteadj = get_keyseq_notes_adjusted(WestTemp, [i]);
            ourseqid = getkeyseqid(ourseqnoteadj);
            if basedone:
                thestring += "<th class=\"text-center chordy\" id=\"%s-0\"><p>%s</p></th>\n" % (ourseqid, i);
            else:
                thestring += "<th class=\"text-center basedone chordy\" id=\"%s-0\"><p>%s</p></th>\n" % (ourseqid, i);
                basedone = True;
            
        thestring += endrow + "</thead>\n<tbody>\n";
        
# Adding new row for base notes.        
#        
#        thestring += startrow; 
#        thestring += "<td>Base note</td>\n";
#        for i in scale.full_notes:
#            thestring += "<td>%s</td>\n" % (i);
#        thestring += endrow;

        for i in scale.rows:
            thestring += startrow;    
            thestring += "<td>%s</td>\n" % i.chord_type;
            for j in i.notes:
                ourseqnoteadj = get_keyseq_notes_adjusted(WestTemp, j.notes);
                ourseqid = getkeyseqid(ourseqnoteadj);
                if not j.chordname_1:
                    thestring += ("<td class=\"chordy\" id = \"%s\" ><p>%s<br />" % (ourseqid, str(j.chordname_1)));
                    thestring += ("<i>%s</i><br />" % (str(j.chordname_2)));
                else:
                    thestring += ("<td class=\"chordy\" id = \"%s\"><p>%s<br />" % (ourseqid, j.notes[0]+" "+str(j.chordname_1)));
                    thestring += ("<i>%s</i><br />" % (j.notes[0]+str(j.chordname_2)));
                    
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
    output = chordgentableneu([value]);
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








