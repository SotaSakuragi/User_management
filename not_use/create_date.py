from db_config import Userdata
from duplicate_confirmation import confirmation


def create_data():
    user_name = input("New user name > ")
    confirmation(user_name)
    user_age = input("New user age > ")
    print(f"Add new user: {user_name}")
    Userdata.create(name=user_name, age=user_age)


if __name__ == "__main__":
    create_data()
