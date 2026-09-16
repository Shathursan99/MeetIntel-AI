from transformers import pipeline

print("Loading Whisper model...")
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

# processor = AutoProcessor.from_pretrained("openai/whisper-small")
# model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-small", device_map="auto")

print("Model loaded successfully!")
print("Transcribing audio..")

result = pipe("test_audio2.mp3")

print("\nTranscription:")
print(result["text"])