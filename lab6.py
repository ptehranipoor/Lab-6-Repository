password = ""


def encode(input_password):
    global password
    for char in input_password:
        password = password + str((int(char) + 3) % 10)


def decode():
    print()


def main():
    is_on = True
    while is_on:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = input("Please enter an option: ")
        num_option = int(option)
        if option == 1:
            user_password = input("Please enter your password to encode: ")
            encode(user_password)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            decode()
        else:
            is_on = False


if __name__ == "__main__":
    main()
