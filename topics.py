import assemblyai as aai

aai.settings.api_key = 'e2f91c4271a140b39806a41fc979e530'

file = "wild.mp3"

transcriber = aai.Transcriber()

config = aai.TranscriptionConfig(iab_categories=True)

transcript = transcriber.transcribe(file, config=config)


for result in transcript.iab_categories.results:
    print(result.text)
    print(f"Timestamp :{result.timestamp.start} - {result.timestamp.end}")
    for label in result.labels:
        print(label.label)
        print(label.relevance)

for label, relevance in transcript.iab_categories.summary.items():
    print(f"Audio is {relevance * 100}% relevant to {label}")

