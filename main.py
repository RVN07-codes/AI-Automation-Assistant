from modules.voice import listen_command
from modules.system import open_app

def start_assistant():
    print("Jarvis online...")

    while True:
        command = listen_command()
        print("Heard:", command)

        if command is None:
            continue

        if "open" in command:
            app = command.replace("open", "").strip()
            response = open_app(app)
            print(response)

        elif "exit" in command or "quit" in command:
            print("Shutting down Jarvis")
            break

start_assistant()
