import speech_recognition as sr
from app_control import (
    open_application,
    focus_window,
    minimize_window,
    restore_window,
    close_window
)

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def handle_command(self, command):
        command = command.lower()
        print(f"🎧 Recognized: {command}")

        if command.startswith("open "):
            app_name = command.replace("open ", "").strip()
            open_application(app_name)
        elif command.startswith("focus "):
            app_name = command.replace("focus ", "").strip()
            focus_window(app_name)
        elif "minimize" in command:
            minimize_window()
        elif "close" in command:
            close_window()
        elif "restore" in command or "maximize" in command:
            restore_window()
        else:
            print("🤷 Command not recognized.")

    def run(self):
        print("🎙️ Say a command (e.g., 'open notepad', 'focus chrome', 'minimize')...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            while True:
                print("🎧 Listening...")
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    command = self.recognizer.recognize_google(audio)
                    self.handle_command(command)
                except sr.WaitTimeoutError:
                    print("⏱️ Listening timed out. Try again...")
                except sr.UnknownValueError:
                    print("❌ Could not understand audio.")
                except sr.RequestError as e:
                    print(f"🔌 API unavailable: {e}")
