from db_config import Userdata


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


def edit_data():
    user_name = input("User name > ")
    print()
    Userdatas = Userdata.select().where(Userdata.name == user_name)
    if Userdatas.exists():
        for userdata in Userdatas:
            userdata.name = input(f"New user name({userdata.name}) > ")
            userdata.age = input(f"New user name({userdata.age}) > ")
            userdata.save()
            print(f"Update user: {userdata.name}")
        return

    else:
        print("名前が見つかりません、正しく入力してください")
        return


def delete_data():
    user_name = input("User name > ")
    Userdatas = Userdata.select().where(Userdata.name == user_name)
    if Userdatas.exists():
        for userdata in Userdatas:
            id = userdata.id
            userdata = Userdata.get_by_id(id)
            userdata.delete_instance()
            print(f"User {user_name} is deleted")

    else:
        print("名前が見つかりません、正しく入力してください")
        return


def find_user():
    user_name = input("User name > ")
    userdatas = Userdata.select().where(Userdata.name == user_name)
    if userdatas.exists():
        for userdata in userdatas:
            print(f"Name: {userdata.name} Age: {userdata.age}")
            return
    else:
        print(f"Sorry, {user_name} is not found")
        return


def create_data():
    user_name = input("New user name > ")
    userdatas = Userdata.select().where(Userdata.name == user_name)
    if userdatas.exists():
        for userdata in userdatas:
            print(f"Duplicated user name {user_name}")
            return
    else:
        user_age = input("New user age > ")
        if not 1 <= len(user_name):
            print("User name can't be blank")
            return
        elif not len(user_name) <= 20:
            print("User name is too long(maximun is 20 characters)")
            return
        elif not user_age.isdigit():
            print("Age is not positive integer")
            return
        elif not 0 <= int(user_age) <= 120:
            print("Age is grater than 120")
            return
        
        print(f"Add new user: {user_name}")
        Userdata.create(name=user_name, age=user_age)
        return


def read_alldata():
    userdatas = Userdata.select()
    for userdata in userdatas:
        print(f"Name: {userdata.name} Age: {userdata.age}")


if __name__ == "__main__":
    main()
