from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

# Path to model folder
model_path = os.path.join(os.path.dirname(__file__), "models", "vosk-model-small-en-us-0.15")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def get_voice_command():
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        return result.get("text", "")
    return ""
