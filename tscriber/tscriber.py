from dotenv import load_dotenv
from google.cloud import speech_v1
from google.cloud.speech import enums
from google.cloud.speech import types
import argparse
import io
import os
from os.path import join, dirname
from dotenv import load_dotenv
from pydub import AudioSegment
from pathlib import Path
import json
import array as arr

##dotenv_path = join(dirname(__file__), 'SECRETS.env')
##load_dotenv(dotenv_path, verbose=True)
##GOOGLE_APPLICATION_CREDENTIALS_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_PATH")

def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using an enhanced model

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1.SpeechClient()

    # local_file_path = 'resources/hello.wav'

    # The enhanced model to use, e.g. phone_call
    # Currently phone_call is the only model available as an enhanced model.
    model = "phone_call"

    # Use an enhanced model for speech recognition (when set to true).
    # Project must be eligible for requesting enhanced models.
    # Enhanced speech models require that you opt-in to data logging.
    use_enhanced = False

    # The language of the supplied audio
    ##language_code = "en-US"
    language_code = "he-IL"
    # Loads the audio into memory
    locpath = Path(local_file_path)
    filename = locpath.stem
    file_extension = locpath.suffix
    if not file_extension == '.wav':
        sound = AudioSegment.from_mp3(locpath)
        sound = sound[:30*1000]
        fs = sound.frame_rate
        dst = os.path.splitext(local_file_path)[0]+'.wav'
        #sound = sound.set_frame_rate(4000)
        sound.export(dst, format="wav")
        local_file_path = dst
    else:
        pass
    with io.open(local_file_path, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=fs,
        language_code='he-IL')

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    #response = client.long_running_recognize(config, audio)
    myfile = open('data/' + filename + '_Transcript.txt', 'w', encoding='utf-8')
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        myfile.write("%s\n" % result.alternatives[0].transcript)
    myfile.close()
    
    #Transcript = {
    #    'filename': filename,
    #    'Transcript': response.results
    #}

    #with open('data/Transcript.json', 'w') as json_file:
    #    json.dump(Transcript, json_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Say hello')
    parser.add_argument('local_file_path', help='Local File Path')
    args = parser.parse_args()

    sample_recognize(args.local_file_path)