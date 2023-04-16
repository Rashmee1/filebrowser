import os
import shutil
import random
import string

class FileBrowsing:
    
        


    def display_menu(self):
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

    def list_dir_contents(self):
        """
        List the contents of the current directory.
        """
        print("Current directory contents:")
        for item in os.listdir(os.getcwd()):
            print(item)
        


    def rename_folder(self):
        """
        Rename a folder in the current directory.
        """
        self.old_name = input("Enter the current folder name: ")
        self.new_name = input("Enter the new folder name: ")
        os.rename(self.old_name, self.new_name)

    def rename_file(self):
        """
        Rename a file in the current directory.
        """
        self.old_name = input("Enter the current file name: ")
        self.new_name = input("Enter the new file name: ")
        os.rename(self.old_name, self.new_name)

    def copy_file(self):
        """
        Copy a file from one location to another.
        """
        self.source = input("Enter the source file path: ")
        self.destination = input("Enter the destination file path: ")
        shutil.copy2(self.source, self.destination)


    def copy_folder(self):
        """
        Copy a folder from one location to another.
        """
        self.source = input("Enter the source folder path: ")
        self.destination = input("Enter the destination folder path: ")
        shutil.copytree(self.source, self.destination)

    def move_file(self):
        """
        Move a file from one location to another.
        """
        self.source = input("Enter the source file path: ")
        self.destination = input("Enter the destination file path: ")
        shutil.move(self.source, self.destination)

    def move_folder(self):
        """
        Move a folder from one location to another.
        """
        self.source = input("Enter the source folder path: ")
        self.destination = input("Enter the destination folder path: ")
        shutil.move(self.source, self.destination)

    def create_empty_file(self):
        """
        Create an empty file in the current directory.
        """
        self.filename = input("Enter the file name: ")
        with open(self.filename, 'w'):
            pass

    def create_text_file_with_random_text(self):
        """
        Create a text file with random text in the current directory.
        """
        self.filename = input("Enter the file name: ")
        list_of_10_random_characters = random.choices(string.ascii_uppercase + string.digits, k=10)
        random_text = ''.join(list_of_10_random_characters)
        with open(self.filename, 'w') as f:
            f.write(random_text)

    def view_file_contents(self):
        """
        View the contents of a file in the current directory.
        """
        self.filename = input("Enter the file name: ")
        with open(filename, 'r') as f:
            contents = f.read()
        print(contents)

    def delete_file(self):
        """
        Delete a file from the current directory.
        """
        self.filename = input("Enter the file name: ")
        os.remove(self.filename)

    def delete_folder(self):
        """
        Delete a folder from the current directory.
        """
        self.foldername = input("Enter the folder name: ")
        shutil.rmtree(self.foldername)

    def hide_folder(self):
        """
        Hide a folder in the current directory.
        """
        self.foldername = input("Enter the folder name: ")
        os.rename(self.foldername, '.' + self.foldername)

    def toggle_hidden_folders(self):
        """
        Toggle the viewing of hidden folders in the current directory.
        """
        self.show_hidden_folders = not os.path.isdir('.hidden')
        if self.show_hidden_folders:
            os.rename('.hidden', 'hidden')
        else:
            os.rename('hidden', '.hidden')

    def make_file_executable(self):
        """
        Make a file executable in the current directory.
        """
        self.filename = input("Enter the file name: ")
        os.chmod(self.filename, 0o755)

