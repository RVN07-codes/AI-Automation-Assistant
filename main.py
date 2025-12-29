from modules.commands import process_command
from modules.voice import listen_command

def start_assistant():
    print("AI Automation Assistant Started")
    print("Say or type 'exit' to stop\n")

    while True:
        mode = input("Type 'v' for voice or 't' for text: ").lower()

        if mode == 'v':
            command = listen_command()
        else:
            command = input(">> ").lower()

        if "exit" in command:
            print("Assistant shutting down.")
            break

        process_command(command)

if __name__ == "__main__":
    start_assistant()
