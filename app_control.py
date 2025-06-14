import subprocess
import pygetwindow as gw
import json

with open("app_paths.json", "r") as f:
    app_paths = json.load(f)

def open_application(app_name):
    if app_name in app_paths:
        try:
            subprocess.Popen(app_paths[app_name])
            print(f"✅ Opening {app_name}")
        except Exception as e:
            print(f"❌ Failed to open {app_name}: {e}")
    else:
        print(f"⚠️ '{app_name}' not found in app_paths.json")

def find_window(app_name):
    for title in gw.getAllTitles():
        if app_name.lower() in title.lower():
            return gw.getWindowsWithTitle(title)[0]
    return None

def focus_window(app_name):
    win = find_window(app_name)
    if win:
        win.activate()
        print(f"🧭 Focused on {win.title}")
    else:
        print(f"❌ Could not find {app_name}")

def minimize_window():
    win = gw.getActiveWindow()
    if win:
        win.minimize()
        print("🟡 Minimized")

def restore_window():
    win = gw.getActiveWindow()
    if win:
        win.restore()
        print("🟢 Restored")

def close_window():
    win = gw.getActiveWindow()
    if win:
        win.close()
        print("❌ Closed")
