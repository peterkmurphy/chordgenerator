#!/usr/bin/python
#-*- coding: UTF-8 -*-
from django.shortcuts import render
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
UNIKEYS = ["C♭", "C", "C♯", "D♭", "D", "E♭", "E", "F", "F♯", "G♭", "G",
    "A♭", "A", "B♭", "B"];

# Rather than using a function to swap between ASCII and Unicode
# equivalents, it seems easier to keep a map. This allows us to look
# for invalid "keys" provided by a malicious user.

MAPKEYS = {"Cb":"C♭", "C#":"C♯", "Db":"D♭", "Eb":"E♭","F#":"F♯",
    "Gb":"G♭", "Ab":"A♭", "Bb":"B♭", "C♭":"Cb", "C♯":"C#", "D♭":"Db",
    "E♭":"Eb", "F♯":"F#", "G♭":"Gb", "A♭":"Ab", "B♭":"Bb"};

MAPSCALES = {"Dorian b9":"Dorian ♭9", "Locrian #6":"Locrian ♯6",
    "Dorian b6":"Dorian ♭6", "Lydian #2 #5":"Lydian ♯2 ♯5",
    "Mixolydian b9":"Mixolydian ♭9", "Phrygian b4":"Phrygian ♭4",
    "Lydian #2":"Lydian ♯2", "Mixolydian b13":"Mixolydian ♭13",
    "Locrian bb7":"Locrian ♭♭7", "Lydian b3":"Lydian ♭3"};

SCALE_ARRAY = list(WestTemp.seq_maps.nseqtype_maps[NSEQ_SCALE].\
    name_dict.keys())

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
            if key in list(MAPKEYS.keys()):
                key = MAPKEYS[key];
            else: # Someone's been playing silly buggers with the GET request.
                key = "C"; # So we return C as simple.
    else:
        key = "C";
    if "scales" in request.GET:
        chosenscale = request.GET["scales"]
        if chosenscale not in SCALE_ARRAY:
            if chosenscale in list(MAPSCALES.keys()):
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
    c = {"keys": keys, "chosenkey": key, "asciiselect":asciiselect,
            "scaletable":scaletable, "scales":scales,
            "chosenscale":chosenscale}
    return render(request, 'chordgenerator/chordgenerator.html', c)
