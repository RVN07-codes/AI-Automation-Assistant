from modules.commands import process_command

def start_assistant():
    print("AI Automation Assistant Started")
    print("Type 'exit' to stop\n")

    while True:
        command = input(">> ").lower()

        if command == "exit":
            print("Assistant shutting down.")
            break

        process_command(command)

if __name__ == "__main__":
    start_assistant()
