import os
import json
import subprocess
from pynput import keyboard

CONFIG_FILE = "shortcuts.json"

def load_shortcuts():
    """Load shortcuts from a JSON configuration file."""
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Error: Configuration file is not a valid JSON.")
            return {}

def save_shortcuts(shortcuts):
    """Save shortcuts to a JSON configuration file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(shortcuts, file, indent=4)

def add_shortcut(shortcuts, key, command):
    """Add a new shortcut."""
    shortcuts[key] = command
    save_shortcuts(shortcuts)
    print(f"Shortcut added: {key} -> {command}")

def remove_shortcut(shortcuts, key):
    """Remove an existing shortcut."""
    if key in shortcuts:
        del shortcuts[key]
        save_shortcuts(shortcuts)
        print(f"Shortcut removed: {key}")
    else:
        print(f"No shortcut found for key: {key}")

def on_activate(shortcuts, key):
    """Execute the command associated with a key."""
    command = shortcuts.get(key.char)
    if command:
        print(f"Launching: {command}")
        subprocess.Popen(command, shell=True)
    else:
        print(f"No command associated with key: {key.char}")

def main():
    shortcuts = load_shortcuts()
    
    listener = keyboard.Listener(
        on_press=lambda key: on_activate(shortcuts, key)
    )
    listener.start()
    
    print("QuickLauncher is running. Press 'Ctrl+C' to exit.")
    try:
        while True:
            print("\nCommands:")
            print("1. Add new shortcut")
            print("2. Remove shortcut")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                key = input("Enter key for shortcut: ")
                command = input("Enter command to execute: ")
                add_shortcut(shortcuts, key, command)
            elif choice == '2':
                key = input("Enter key to remove: ")
                remove_shortcut(shortcuts, key)
            elif choice == '3':
                print("Exiting QuickLauncher.")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nQuickLauncher terminated.")

if __name__ == "__main__":
    main()