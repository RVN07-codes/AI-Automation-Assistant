import subprocess
import os

def open_app(app_name):
    app_name = app_name.lower().strip()

    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": r"C:\Users\Apple\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }

    # normalize speech variations
    aliases = {
        "vs code": "vscode",
        "visual studio code": "vscode",
        "google chrome": "chrome"
    }

    if app_name in aliases:
        app_name = aliases[app_name]

    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name])
            return f"Opening {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}"
    else:
        return "Application not found"
