#!/usr/bin/python 
#-*- coding: UTF-8 -*-
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect;
from django.template.response import TemplateResponse;
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.html import strip_tags
from musictheory.temperament import WestTemp, temperament, seq_dict,\
    NSEQ_SCALE, NSEQ_CHORD, M_SHARP, M_FLAT, un_unicode_accdtls;
from musictheory.scales import MajorScale, MelMinorScale, HarmMinorScale,\
    HarmMajorScale;
from musictheory.chordgenerator import populate_scale_chords, \
    CHORDTYPE_ARRAY;

# The two sequences list the 15 standard musical keys in ASCII and Unicode
# formats.

ASCIIKEYS = ["Cb", "C", "C#", "Db", "D", "Eb", "E", "F", "F#", "Gb", "G",
    "Ab", "A", "Bb", "B"];
UNIKEYS = [u"C♭", "C", u"C♯", u"D♭", "D", u"E♭", "E", "F", u"F♯", u"G♭", "G",
    u"A♭", "A", u"B♭", "B"];

# Rather than using a function to swap between ASCII and Unicode
# equivalents, it seems easier to keep a map. This allows us to look
# for invalid "keys" provided by a malicious user.

MAPKEYS = {"Cb":u"C♭", "C#":u"C♯", "Db":u"D♭", "Eb":u"E♭","F#":u"F♯", 
    "Gb":u"G♭", "Ab":u"A♭", "Bb":u"B♭", u"C♭":"Cb", u"C♯":"C#", u"D♭":"Db",
    u"E♭":"Eb", u"F♯":"F#", u"G♭":"Gb", u"A♭":"Ab", u"B♭":"Bb"};

MAPSCALES = {"Dorian b9":u"Dorian ♭9", "Locrian #6":u"Locrian ♯6", 
    "Dorian b6":u"Dorian ♭6", "Lydian #2 #5":u"Lydian ♯2 ♯5", 
    "Mixolydian b9":u"Mixolydian ♭9", "Phrygian b4":u"Phrygian ♭4",
    "Lydian #2":u"Lydian ♯2", "Mixolydian b13":u"Mixolydian ♭13",
    "Locrian bb7":u"Locrian ♭♭7", u"Lydian b3":u"Lydian ♭3"};

SCALE_ARRAY = WestTemp.seq_maps.nseqtype_maps[NSEQ_SCALE].\
    name_dict.keys()

def index(request):
    """ Contains explanatory text. Nothing needs to be loaded. """
    if "asciif" in request.GET and request.GET["asciif"] == "asciif":
        keys = ASCIIKEYS
        asciiselect = True;
    else:
        keys = UNIKEYS;
        asciiselect = False;
    if "key" in request.GET:
        key = request.GET["key"]
        if key not in keys:
            if key in MAPKEYS.keys():
                key = MAPKEYS[key];
            else: # Someone's been playing silly buggers with the GET request.
                key = "C"; # So we return C as simple.
    else:
        key = "C";
    if "scales" in request.GET:
        chosenscale = request.GET["scales"]
        if chosenscale not in SCALE_ARRAY:
            if chosenscale in MAPSCALES.keys():
                chosenscale = MAPSCALES[chosenscale];
            else: # Again, enemy action from the GET request.
                chosenscale = "Major";
    else:
        chosenscale = "Major"
    scaletable = populate_scale_chords(chosenscale, key, CHORDTYPE_ARRAY)
    if asciiselect:
        scales = sorted([un_unicode_accdtls(i) for i in SCALE_ARRAY]);
        chosenscale = un_unicode_accdtls(chosenscale);
    else:
        scales = sorted(SCALE_ARRAY);
    c = RequestContext(request, {"keys": keys, "chosenkey": key, "asciiselect":asciiselect,
        "scaletable":scaletable, "scales":scales, 
        "chosenscale":chosenscale})
    return TemplateResponse(request, 'chordgenerator/chordgenerator.html', context=c)


