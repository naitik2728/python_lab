
import os
import sys


def show_directory(path):
    """Display files and folders in a directory."""
    print("\nContents of:", path)

    try:
        items = os.listdir(path)

        if not items:
            print("Directory is empty.")
            return

        for item in items:
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                print("[DIR] ", item)
            else:
                print("[FILE]", item)

    except PermissionError:
        print("Permission denied.")


def list_extension(path, extension):
    """List files having a particular extension."""
    print("\nFiles with", extension, "extension:")

    try:
        for item in os.listdir(path):
            if item.endswith(extension):
                print(item)

    except PermissionError:
        print("Permission denied.")


def create_workspace(path):
    """Create a workspace directory."""
    workspace = os.path.join(path, "workspace")

    if not os.path.exists(workspace):
        os.mkdir(workspace)
        print("Workspace created:", workspace)
    else:
        print("Workspace already exists:", workspace)


def create_log(path):
    """Create/read a text log using context manager."""
    log_file = os.path.join(path, "system_log.txt")

    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            file.write("System Utility Log\n")
            file.write("Log file created successfully.\n")

        print("Log file created:", log_file)

    else:
        print("\nExisting log file:")
        with open(log_file, "r") as file:
            print(file.read())


# ---------------- MAIN PROGRAM ----------------

# Check command-line argument
if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    directory = os.getcwd()

# Check whether directory exists
if not os.path.exists(directory):
    print("Error: Directory does not exist.")
    sys.exit(1)

if not os.path.isdir(directory):
    print("Error: Path is not a directory.")
    sys.exit(1)


while True:
    print("\n========== FILE MANAGEMENT UTILITY ==========")
    print("Current Directory:", directory)
    print("1. Show Directory Contents")
    print("2. Navigate to Subdirectory")
    print("3. Create Workspace")
    print("4. List Python Files")
    print("5. Create/Read System Log")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_directory(directory)

    elif choice == "2":
        folder = input("Enter subdirectory name: ")
        new_path = os.path.join(directory, folder)

        if os.path.isdir(new_path):
            directory = os.path.abspath(new_path)
            print("Moved to:", directory)
        else:
            print("Subdirectory not found.")

    elif choice == "3":
        create_workspace(directory)

    elif choice == "4":
        list_extension(directory, ".py")

    elif choice == "5":
        create_log(directory)

    elif choice == "6":
        print("Exiting utility...")
        break

    else:
        print("Invalid choice.")