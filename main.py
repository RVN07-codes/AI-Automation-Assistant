import os
import subprocess
import psutil
import speech_recognition as sr

# ------------------ VOICE INPUT ------------------
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
        return ""
    except sr.RequestError:
        print("Speech service error.")
        return ""

# ------------------ APP FINDING (DYNAMIC) ------------------
START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    r"C:\Users\Apple\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
]

def find_app(app_name):
    for base_path in START_MENU_PATHS:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if app_name in file.lower() and file.endswith(".lnk"):
                    return os.path.join(root, file)
    return None

# ------------------ OPEN APP ------------------
def open_app(app_name):
    app_path = find_app(app_name)

    if app_path:
        subprocess.Popen(f'explorer "{app_path}"')
        return f"Opening {app_name}"
    else:
        return "Application not found"

# ------------------ CLOSE APP ------------------
def close_app(app_name):
    closed = False
    for proc in psutil.process_iter(['name']):
        try:
            if app_name in proc.info['name'].lower():
                proc.kill()
                closed = True
        except:
            pass

    if closed:
        return f"Closed {app_name}"
    else:
        return "Application not running"

# ------------------ MAIN LOOP ------------------
def start_assistant():
    print("Jarvis online...")

    while True:
        command = listen_command()

        if not command:
            continue

        if command.startswith("open"):
            app = command.replace("open", "", 1).strip()
            print(open_app(app))

        elif command.startswith("close"):
            app = command.replace("close", "", 1).strip()
            print(close_app(app))

        elif "exit" in command or "quit" in command:
            print("Shutting down Jarvis")
            break

        else:
            print("Command not recognized")

# ------------------ RUN ------------------
if __name__ == "__main__":
    start_assistant()
