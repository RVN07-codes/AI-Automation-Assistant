import webbrowser
import datetime
import os

def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)

    elif "date" in command:
        current_date = datetime.date.today()
        print("Today's Date:", current_date)

    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        print("Opening browser...")

    elif "open notepad" in command:
        os.system("notepad")

    else:
        print("Command not recognized.")
