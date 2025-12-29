import os
import subprocess

def open_app(app_name):
    app_name = app_name.lower()

    apps = {
        "chrome": "chrome",
        "vscode": "code",
        "notepad": "notepad",
        "calculator": "calc",
        "cmd": "cmd"
    }

    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name], shell=True)
            return f"Opening {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}"
    else:
        return "Application not found"
