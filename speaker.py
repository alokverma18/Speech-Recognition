import assemblyai as aai

aai.settings.api_key = 'e2f91c4271a140b39806a41fc979e530'

file = "wild.mp3"

transcriber = aai.Transcriber()

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(file, config=config)


for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker} : {utterance.text}")
