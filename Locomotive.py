# Imports the hash function from the python standard library
import hashlib
# Imports the os function from the python standard library
import os
# Imports TK which is the main windows of a GUI
from tkinter import Tk
# Imports askopenfilename which allows the user to select a file from the file browser, and askdirectory which allows the user to select a folder/directory from the file browser.
from tkinter.filedialog import askopenfilename, askdirectory


# Displays welcome message and then menu options for user input
def display_menu():
    # Displays the welcome message, the description of this tool, and the options
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
    print("3. Calculate and Compare the SHA-256 hash of many files")
    print("4. Calculate and Compare the SHA-256 hash of folders")
    print("5. Exit")
    print(" ")
    print("------------------")
    print(" ")

    # Asks for the user to select an option from the above list
    user_choice = input("Select an option: ")
    return user_choice


# This will take the file path desired and then calculate the SHA-256 hash and return that value
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    try:
        # This opens the file in read binary and processes it in 4096 chunks
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                sha256_hash.update(chunk)
    except FileNotFoundError:
        # Error Handling for when a file is not found
        print(f"File not found: {file_path}")
        return None

    except PermissionError:
        # Error Handling for when permissions are denied
        print(f"Permission denied: {file_path}")
        return None

    except Exception as e:
        # Error Handling for when general errors may occur
        print(f"Error has occurred while calculating hash: {e}")
        return None

    # Changes the file hash to a hexadecimal format
    file_hash = sha256_hash.hexdigest()
    return file_hash


# This will prompt the user to select a file using the popup file dialog box
def select_file():
    root = Tk()
    root.withdraw()
    file_path = askopenfilename(title="Select a file")
    return file_path


# This will prompt the user to select a folder using the popup file dialog box
def select_folder():
    root = Tk()
    root.withdraw()
    folder_path = askdirectory(title="Select a folder")
    return folder_path


# Program loop for the choices
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
        print(" ")
        input("You selected option {}. "
              "When the popup dialog box appears, select your files. Press enter to continue...".format(choice))

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
        print(f"File 2: {file_path2}")
        print(f"SHA-256 Hash:", hash_value2)

        if hash_value1 == hash_value2:
            print("Good News! These files have the same hash value, they must be identical")
        else:
            print("WARNING!!! These files do not have the same hash value. Integrity may be compromised")

    # Option 3 - Creates the SHA-356 Hash of multiple files and compares them
    elif choice == "3":
        print(" ")
        input("You selected option {}. "
              "When the popup dialog box appears, select your files. Press enter to continue...".format(choice))

        file_names = []
        hashes = []
        while True:
            file_path = select_file()
            if not file_path:
                print("No file selected.")
                break

            hash_value = calculate_sha256(file_path)
            if hash_value:
                print(f"File: {file_path}")
                print(f"SHA-256 Hash: {hash_value}")
                file_names.append(file_path)
                hashes.append(hash_value)

            another_file = input("Would you like to select another file for comparison? (yes/no): ")
            if another_file.lower() == 'no':
                break
            elif another_file.lower() != 'yes':
                continue

        if len(hashes) < 2:
            print("At least two files are needed")
        else:
            all_same = all(value == hashes[0] for value in hashes)
            comparison_status = "Good News! All of these files have the same hash value, they must be identical" if all_same else "WARNING!!! These files do not have the same hash value. Integrity may be compromised"

            print(" ")
            print(comparison_status)

            for i in range(len(file_names)):
                print(" ")
                print("***********************************************************************************************")
                print(f"File: {file_names[i]}")
                print(f"SHA-256 Hash: {hashes[i]}")
                print("***********************************************************************************************")
                print(" ")

            print(comparison_status)

    # Option 4 - Calculates and compares the hashes for the selected folders
    elif choice == "4":
        print(" ")
        input(" You selected option {} . "
              "When the popup dialog appears, select the folder. Press enter to continue...".format(choice))

        try:
            folder_path1 = select_folder()
            if not folder_path1:
                print("No folder was selected.")
                continue

            folder_path2 = select_folder()
            if not folder_path2:
                print("No folder was selected.")
                continue

            files1 = []
            hashes1 = []
            for root, _, files in os.walk(folder_path1):
                for file in files:
                    file_path = os.path.join(root, file)
                    hash_value = calculate_sha256(file_path)
                    if hash_value:
                        files1.append(file_path)
                        hashes1.append(hash_value)

            files2 = []
            hashes2 = []
            for root, _, files in os.walk(folder_path2):
                for file in files:
                    file_path = os.path.join(root, file)
                    hash_value = calculate_sha256(file_path)
                    if hash_value:
                        files2.append(file_path)
                        hashes2.append(hash_value)

            if not files1 or not files2:
                print("No files found in the selected folders.")
                continue

            if len(files1) != len(files2):
                print("The number of files in the two folders is different.")
                continue

            all_same = True
            for file1, file2 in zip(files1, files2):
                if calculate_sha256(file1) != calculate_sha256(file2):
                    all_same = False
                    break

            comparison_status = "Good News! All of these files have the same hash value, they must be identical" if all_same else "WARNING!!! These files do not have the same hash value. Integrity may be compromised"

            print(" ")
            print(comparison_status)

            for i in range(len(files1)):
                print(" ")
                print("***********************************************************************************************")
                print(f"File 1: {files1[i]}")
                print(f"SHA-256 Hash 1: {hashes1[i]}")
                print(f"File 2: {files2[i]}")
                print(f"SHA-256 Hash 2: {hashes2[i]}")
                print("***********************************************************************************************")
                print(" ")

            print(" ")
            print(comparison_status)

        except Exception as e:
            print(f"Error occurred while processing folders: {e}")


    # Option 5 - Exits the program
    elif choice == "5":
        print("Exiting...")
        break

    # If anything other than the 5 options are selected, returns this message.
    else:
        print("Invalid choice selected. Please select a valid option or exit the program.")
