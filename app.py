from tools import create_data, read_alldata, find_user, delete_data, edit_data


def main():
    with open("welcome.txt", "r") as file:  # 最初の文字列をtextからprint
        content = file.read()
    print(content)
    condition()


def condition():
    while True:
        command = input("Your command > ")
        if command == "S" or command == "s":
            read_alldata()
        elif command == "A" or command == "a":
            create_data()
        elif command == "Q" or command == "q":
            print("Bye!")
            return
        elif command == "F" or command == "f":
            find_user()
        elif command == "D" or command == "d":
            delete_data()
        elif command == "E" or command == "e":
            edit_data()
        else:
            print(f"{command}: command not found")
        print()


if __name__ == "__main__":
    main()
