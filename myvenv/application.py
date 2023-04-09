import os
import shutil
import random
import string

def display_menu():
    """
    Display the menu of options for the file browser application.
    """
 
    print("1. List the contents of the current directory")
    print("2. Rename a folder in the current directory")
    print("3. Rename a file in the current directory")
    print("4. Copy a file from one location to another")
    print("5. Copy a folder from one location to another")
    print("6. Move a file from one location to another")
    print("7. Move a folder from one location to another")
    print("8. Create an empty file in the current directory")
    print("9. Create a text file with random text in the current directory")
    print("10. View the contents of a file in the current directory")
    print("11. Delete a file from the current directory")
    print("12. Delete a folder from the current directory")
    print("13. Hide a folder in the current directory")
    print("14. Toggle the viewing of hidden folders in the current directory")
    print("15. Make a file executable in the current directory")
    print("q. Quit the application")

def list_directory_contents():
    """
    List the contents of the current directory.
    """
    print("Current directory contents:")
    for item in os.listdir(os.getcwd()):
        print(item)

def rename_folder():
    """
    Rename a folder in the current directory.
    """
    old_name = input("Enter the current folder name: ")
    new_name = input("Enter the new folder name: ")
    os.rename(old_name, new_name)

def rename_file():
    """
    Rename a file in the current directory.
    """
    old_name = input("Enter the current file name: ")
    new_name = input("Enter the new file name: ")
    os.rename(old_name, new_name)

def copy_file():
    """
    Copy a file from one location to another.
    """
    source = input("Enter the source file path: ")
    destination = input("Enter the destination file path: ")
    shutil.copy2(source, destination)


def copy_folder():
    """
    Copy a folder from one location to another.
    """
    source = input("Enter the source folder path: ")
    destination = input("Enter the destination folder path: ")
    shutil.copytree(source, destination)

def move_file():
    """
    Move a file from one location to another.
    """
    source = input("Enter the source file path: ")
    destination = input("Enter the destination file path: ")
    shutil.move(source, destination)

def move_folder():
    """
    Move a folder from one location to another.
    """
    source = input("Enter the source folder path: ")
    destination = input("Enter the destination folder path: ")
    shutil.move(source, destination)

def create_empty_file():
    """
    Create an empty file in the current directory.
    """
    filename = input("Enter the file name: ")
    with open(filename, 'w'):
        pass

def create_text_file_with_random_text():
    """
    Create a text file with random text in the current directory.
    """
    filename = input("Enter the file name: ")
    random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    with open(filename, 'w') as f:
        f.write(random_text)

def view_file_contents():
    """
    View the contents of a file in the current directory.
    """
    filename = input("Enter the file name: ")
    with open(filename, 'r') as f:
        contents = f.read()
    print(contents)

def delete_file():
    """
    Delete a file from the current directory.
    """
    filename = input("Enter the file name: ")
    os.remove(filename)

def delete_folder():
    """
    Delete a folder from the current directory.
    """
    foldername = input("Enter the folder name: ")
    shutil.rmtree(foldername)

def hide_folder():
    """
    Hide a folder in the current directory.
    """
    foldername = input("Enter the folder name: ")
    os.rename(foldername, '.' + foldername)

def toggle_hidden_folders():
    """
    Toggle the viewing of hidden folders in the current directory.
    """
    show_hidden_folders = not os.path.isdir('.hidden')
    if show_hidden_folders:
        os.rename('.hidden', 'hidden')
    else:
        os.rename('hidden', '.hidden')

def make_file_executable():
    """
    Make a file executable in the current directory.
    """
    filename = input("Enter the file name: ")
    os.chmod(filename, 0o755)

