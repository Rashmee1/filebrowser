import application
while True:
    application.display_menu()
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        application.list_directory_contents()
    elif user_choice == "2":
        application.rename_folder()
    elif user_choice == "3":
        application.rename_file()
    elif user_choice == "4":
        application.copy_file()
    elif user_choice == "5":
        application.copy_folder()
    elif user_choice == "6":
        application.move_file()
    elif user_choice == "7":
        application.move_folder()
    elif user_choice == "8":
        application.create_empty_file()
    elif user_choice == "9":
        application.create_text_file_with_random_text()
    elif user_choice == "10":
        application.view_file_contents()
    elif user_choice == "11":
        application.delete_file()
    elif user_choice == "12":
        application.delete_folder()
    elif user_choice == "13":
        application.hide_folder()
    elif user_choice == "14":
        application.toggle_hidden_folders()
    elif user_choice == "15":
        application.make_file_executable()
    elif user_choice == "q":
        break
    else:
        print("Invalid choice. Please try again.")


