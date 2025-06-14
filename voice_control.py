import speech_recognition as sr
import pyttsx3
import webbrowser

from app_control import (
    open_application, focus_window, minimize_window,
    restore_window, close_window, switch_to_window,
    list_open_apps, take_screenshot
)

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)

    def speak(self, message):
        print(f"🗣️ {message}")
        self.engine.say(message)
        self.engine.runAndWait()

    def handle_command(self, command):
        command = command.lower()
        print(f"🎧 Recognized: {command}")

        if command.startswith("open "):
            app_name = command.replace("open ", "").strip()
            open_application(app_name)
            self.speak(f"Opening {app_name}")
        elif command.startswith("focus "):
            app_name = command.replace("focus ", "").strip()
            focus_window(app_name)
            self.speak(f"Focusing on {app_name}")
        elif command.startswith("switch to "):
            app_name = command.replace("switch to ", "").strip()
            switch_to_window(app_name)
            self.speak(f"Switched to {app_name}")
        elif "minimize" in command:
            minimize_window()
            self.speak("Window minimized")
        elif "restore" in command or "maximize" in command:
            restore_window()
            self.speak("Window restored")
        elif "close" in command:
            close_window()
            self.speak("Window closed")
        elif "list apps" in command:
            titles = list_open_apps()
            self.speak("Opened apps are: " + ", ".join(titles))
        elif "take screenshot" in command:
            take_screenshot()
            self.speak("Screenshot taken and saved")
        elif command.startswith("open website"):
            site = command.replace("open website", "").strip()
            webbrowser.open(f"https://{site}.com")
            self.speak(f"Opening {site}.com")
        else:
            self.speak("Sorry, I didn't understand that command.")

    def run(self):
        self.speak("Voice assistant started. Say your command.")
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
