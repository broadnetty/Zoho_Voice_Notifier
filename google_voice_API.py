#!/usr/bin/python

from google.cloud import texttospeech
import os, sys

# Instantiates a client
client = texttospeech.TextToSpeechClient()

ssml='<speak>  Here are <say-as interpret-as="characters">SSML</say-as> samples.  I can pause <break time="3s"/>.  I can play a sound  <audio src="https://www.example.com/MY_MP3_FILE.mp3">didn\'t get your MP3 audio file</audio>.  I can speak in cardinals. Your number is <say-as interpret-as="cardinal">10</say-as>.  Or I can speak in ordinals. You are <say-as interpret-as="ordinal">10</say-as> in line.  Or I can even speak in digits. The digits for ten are <say-as interpret-as="characters">10</say-as>.  I can also substitute phrases, like the <sub alias="World Wide Web Consortium">W3C</sub>.  Finally, I can speak a paragraph with two sentences.  <p><s>This is sentence one.</s><s>This is sentence two.</s></p></speak>'
# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)#text="You have 3 emails. 1st from Nicolas: How to make my backups work? ")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-gb',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

print("Playing MP3..")

os.system('cmdmp3\cmdmp3win.exe output.mp3')
print('done.')