from application import *
def main():
    test= FileBrowsing()
    while True:
        test.display_menu()

        choice = input("Enter your choice: ")
        if choice == 'q':
            break
        elif choice == '1':
            test.list_dir_contents()
        elif choice == '2':
            test.rename_folder()
        elif choice == '3':
            test.rename_file()
        elif choice == '4':
            test.copy_file()
        elif choice == '5':
            test.copy_folder()
        elif choice == '6':
            test.move_file()
        elif choice == '7':
            test.move_folder()
        elif choice == '8':
            test.create_empty_file()
        elif choice == '9':
            test.create_text_file_with_random_text()
        elif choice == '10':
            test.view_file_contents()
        elif choice == '11':
            test.delete_file()
        elif choice == '12':
            test.delete_folder()
        elif choice == '13':
            test.hide_folder()
        elif choice == '14':
            test.toggle_hidden_folders()
        elif choice == '15':
            test.make_file_executable()
            
        else:
            print("Invalid choice!")

main()