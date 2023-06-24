import hashlib
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Displays welcome message and then menu options for user input
def display_menu():
    print(" ")
    print("*******************************************************************************************************************************")
    print("Locomotive is an open source security tool that can assist an entry level security professional with simple security automation")
    print("*******************************************************************************************************************************")
    print(" ")
    print("------ Menu ------")
    print(" ")
    print("1. Calculate SHA-256 hash of a file")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    print(" ")
    print("------------------")
    print(" ")

    choice = input("Select an option: ")
    return choice

# This will take the file path desired and then calculate a SHA-256 hash and return that value
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256_hash.update(chunk)

    file_hash = sha256_hash.hexdigest()
    return file_hash

# This will prompt the user to select a file using the popup file dialog
def select_file():
    root = Tk()
    root.withdraw()
    file_path = askopenfilename(title="Select a file")
    return file_path

# The program loop for choices
while True:
    choice = display_menu()

    if choice == "1":
        file_path = select_file()
        if file_path:
            hash_value = calculate_sha256(file_path)
            print("SHA-256 Hash:", hash_value)
        else:
            print("No file selected.")

    elif choice == "2":
        # Option 2 implementation
        print("Running Option 2")

    elif choice == "3":
        # Option 3 implementation
        print("Running Option 3")

    elif choice == "4":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
