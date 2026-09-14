from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")

from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

processor = AutoProcessor.from_pretrained("openai/whisper-small")
model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-small", device_map="auto")