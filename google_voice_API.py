#!/usr/bin/python3

from google.cloud import texttospeech
import os
import platform
import json

class SynthSpeaker:
    #Load config from config.json
    def __init__(self):
        config_path="config.json"

        #checking for alternate config path
        if 'ZOHO_SPEAKER_CONFIG_PATH' in os.environ:
            config_path = os.environ['ZOHO_SPEAKER_CONFIG_PATH']

        #loading credentials downloaded
        with open(config_path) as fileconf:
            self.config = json.load(fileconf)
            if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.config['config']['voice']['auth_json_path']

        self.setup('data')

        if 'linux' in platform.system():
            self.config['config']['voice']['mp3player_cmd'] = 'mplayer'
            self.config['config']['voice']['mp3_params'] = '> /dev/null 2>&1'
        return


    def download(self, text2say):
        try:
            client = texttospeech.TextToSpeechClient()
            response = client.synthesize_speech(text2say, self.voice, self.audio_config)
            # The response's audio_content is binary.
            with open(self.config['config']['voice']['temp_mp3_path'], 'wb') as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
            return self.config['config']['voice']['temp_mp3_path']
        except Exception:
        #say if there was error
            return 'API_error.mp3'


    def play(self, file_path):
        print("Playing MP3..")
        os.system(self.config['config']['voice']['mp3player_cmd'] + ' '
                  + file_path + ' ' +
                  self.config['config']['voice']['mp3_params'])
        print('done.')
        return

    def say(self, text):
        #Starting player with path returned
        self.play(self.download(texttospeech.types.SynthesisInput(ssml=text)))
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



#speaker = SynthSpeaker()
#text = ''
#with open('tempsubj.txt', 'r') as src:
#    text += str(src.readlines()) + '\n'
#speaker.say(text)