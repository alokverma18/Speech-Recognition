import assemblyai as aai

aai.settings.api_key = 'e2f91c4271a140b39806a41fc979e530'

file = "wild.mp3"

transcriber = aai.Transcriber()

config = aai.TranscriptionConfig(summarization=True)

transcript = transcriber.transcribe(file, config=config)

print(transcript.summary)

