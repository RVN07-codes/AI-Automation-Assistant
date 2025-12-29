import os
import subprocess

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    r"C:\Users\Apple\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
]

def find_app(app_name):
    app_name = app_name.lower()

    for base_path in START_MENU_PATHS:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if app_name in file.lower() and file.endswith(".lnk"):
                    return os.path.join(root, file)
    return None

def open_any_app(app_name):
    app_path = find_app(app_name)

    if app_path:
        subprocess.Popen(f'explorer "{app_path}"')
        return f"Opening {app_name}"
    else:
        return "App not found on system"

def close_app(app_name):
    app_name = app_name.lower()

    closed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if app_name in proc.info['name'].lower():
                proc.kill()
                closed = True
        except:
            pass

    if closed:
        return f"Closed {app_name}"
    else:
        return "App not running"
