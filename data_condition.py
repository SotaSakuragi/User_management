from read_all import read_alldata
from create_date import create_data


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
        else:
            print(f"{command}: command not found")
        print()


if __name__ == "__main__":
    condition()
