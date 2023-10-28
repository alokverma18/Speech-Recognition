import assemblyai as aai

aai.settings.api_key = 'e2f91c4271a140b39806a41fc979e530'

file = "wild.mp3"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(file)

print(transcript.text)
