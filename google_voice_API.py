#!/usr/bin/python3

from google.cloud import texttospeech
import os, sys,platform
import json


class SynthSpeaker():

    #Load config from config.json
    def __init__(self):
        config_path="config.json"

        #checking for alternate config path
        if 'ZOHO_SPEAKER_CONFIG_PATH' in os.environ:
            config_path = os.environ['ZOHO_SPEAKER_CONFIG_PATH']

        #loading credentials downloaded
        with open(config_path) as fileconf:
            self.config = json.load(fileconf)
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.config['config']['voice']['auth_json_path']

        self.setup('data')
        return


    def download(self, text):
        try:
            client = texttospeech.TextToSpeechClient()
            response = client.synthesize_speech(text, self.voice, self.audio_config)
        except Exception:
            self.play('API_error.mp3')

        # The response's audio_content is binary.
        with open(self.config['config']['voice']['temp_mp3_path'], 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
        return

    def play(self, file_path):
        print("Playing MP3..")

        os.system(self.config['config']['voice']['mp3player_cmd'] + ' '
                  + file_path + ' ' +
                  self.config['config']['voice']['mp3_params'])
        print('done.')
        return

    def say(self, text):
        self.download(texttospeech.types.SynthesisInput(text=text))
        self.play(self.config['config']['voice']['temp_mp3_path'])
        return

    def setup(self, data):
        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-ir',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        # Select the type of audio file you want returned
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        return



speaker = SynthSpeaker()
text = ''
with open('tempsubj.txt', 'r') as src:
    text += str(src.readlines()) + '\n'
speaker.say(text)