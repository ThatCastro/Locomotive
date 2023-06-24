import hashlib
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Displays welcome message and then menu options for user input
def display_menu():
    print(" ")
    print(
        "*************************************************************************************************************")
    print(
        "Locomotive is an open source security tool that can assist with simple security automation")
    print(
        "*************************************************************************************************************")
    print(" ")
    print("------ Menu ------")
    print(" ")
    print("1. Calculate SHA-256 hash of a file")
    print("2. Calculate and Compare the SHA-256 hash of two files")
    print("3. Option 3")
    print("4. Exit")
    print(" ")
    print("------------------")
    print(" ")

    user_choice = input("Select an option: ")
    return user_choice


# This will take the file path desired and then calculate the SHA-256 hash and return that value
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

    # Option 1 - Creates the SHA-256 Hash of a selected file
    if choice == "1":

        print(" ")
        input("You selected option {}. "
              "When the popup dialog box appears, select your file. Press enter to continue...".format(choice))

        file_path = select_file()
        if file_path:
            hash_value = calculate_sha256(file_path)
            print(" ")
            print("SHA-256 Hash:", hash_value)
        else:
            print("No file selected.")

    # Option 2 - Creates the SHA-256 Hash of File1 and File2 and compares them
    elif choice == "2":
        file_path1 = select_file()
        if not file_path1:
            print("No file selected.")
            continue

        hash_value1 = calculate_sha256(file_path1)
        print(f"File 1: {file_path1}")
        print(f"SHA-256 Hash:", hash_value1)

        file_path2 = select_file()
        if not file_path2:
            print("No file selected.")
            continue

        hash_value2 = calculate_sha256(file_path2)
        print(f"File 2: {file_path1}")
        print(f"SHA-256 Hash:", hash_value2)

        if hash_value1 == hash_value2:
            print("Good News! These files have the same hash value")
        else:
            print("WARNING!!! These files do not have the same hash value. Integrity may be compromised")

    elif choice == "3":
        # Option 3 implementation
        print("Running Option 3")

    elif choice == "4":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
