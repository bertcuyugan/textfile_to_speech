#!/usr/bin/python3

from gtts import gTTS
import os

# Language selected
language = 'en'

# Opening the text file for speech
file = open("/mnt/hgfs/python-projects/personal project/textfile_to_speech/textfile_to_speech/textfile3.txt", "r").read().replace("\n", " ")

# The speech reading the text file
speech = gTTS(text = str('textfile3.txt'), lang = language, slow = False)

# Save the speech
speech.save("/mnt/hgfs/python-projects/personal project/textfile_to_speech/textfile_to_speech/textfile3_v2.mp3")


# Play the speech
from playsound import playsound

playsound("/mnt/hgfs/python-projects/personal project/textfile_to_speech/textfile_to_speech/textfile3_v2.mp3")
