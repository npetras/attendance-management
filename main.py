from admin import Admin

EXIT = 5

if __name__ == '__main__':

    print_menu()
    choice = input("")
    while choice != EXIT:
        print_menu()
        choice = input("")

