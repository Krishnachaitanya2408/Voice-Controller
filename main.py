from voice_control import get_voice_command
from app_control import focus_window, perform_action

def main():
    print("🎤 Voice Assistant Running (say 'exit' to quit)")
    print("Try commands like: 'focus chrome', 'click', 'scroll down', 'screenshot'\n")

    while True:
        command = get_voice_command()
        if command:
            command = command.lower().strip()
            print(f"🗣 You said: '{command}'")

            if "exit" in command:
                print("👋 Exiting...")
                break
            elif command.startswith("focus "):
                app_name = command.replace("focus", "").strip()
                if not focus_window(app_name):
                    print(f"❌ Could not find window with '{app_name}'")
            else:
                perform_action(command)

if __name__ == '__main__':
    main()
