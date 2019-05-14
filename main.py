import encryption
import utils


def main():
    should_exit = False
    while should_exit is False:
        utils.print_menu()
        option = input()
        if option == "szyfrowanie":
            utils.print_text()
            utils.print_result(encryption.encrypt(input()))
        elif option == "deszyfrowanie":
            utils.print_text()
            utils.print_result(encryption.decrypt(input()))
        elif option == "wyjscie":
            should_exit = True
        else:
            utils.print_error()
    utils.print_end()


if __name__ == "__main__":
    main()
