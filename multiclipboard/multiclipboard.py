import sys
import clipboard
import json

MULTICLIPBOARD_FILEPATH = "multiclipboard.json"


def save_multiclipboard(filepath, multiclipboard):
    with open(filepath, "w") as file:
        json.dump(multiclipboard, file)


def load_multiclipboard(filepath):
    try:
        with open(filepath, "r") as file:
            multiclipboard = json.load(file)
            return multiclipboard
    except:
        return {}


args = sys.argv[1:]

if len(args) == 1:
    command = args[0]
    data = load_multiclipboard(MULTICLIPBOARD_FILEPATH)

    if command == "save":
        key = input("Enter a key to save to: ")
        data[key] = clipboard.paste()
        save_multiclipboard(MULTICLIPBOARD_FILEPATH, data)
        print("Data saved to multiclipboard.")

    elif command == "load":
        key = input("Enter a key to load from: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data loaded from multiclipboard.")
        else:
            print("That key does not exist.")

    elif command == "delete":
        key = input("Enter a key to delete data for: ")
        del data[key]
        save_multiclipboard(MULTICLIPBOARD_FILEPATH, data)
        print("Data deleted from multiclipboard.")

    elif command == "clear":
        data = {}
        save_multiclipboard(MULTICLIPBOARD_FILEPATH, data)
        print("Data cleared from multiclipboard.")

    elif command == "list":
        for key, value in data.items():
            print(f'\n{key}: {value}')

    else:
        print("Unknown command.")
else:
    print("You may only enter one command at a time.")
