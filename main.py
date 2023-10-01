from db_config import Userdata


def main():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")
    print()
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
        else:
            print(f"{command}: command not found")
        print()


def create_data():
    user_name = input("New user name > ")
    user_age = input("New user age > ")
    print(f"Add new user: {user_name}")
    Userdata.create(name=user_name, age=user_age)


def read_alldata():
    userdates = Userdata.select()
    for userdate in userdates:
        print(f"Name: {userdate.name} Age: {userdate.age}")


if __name__ == "__main__":
    main()
