from db_config import Userdata


def display_all_userdata():
    userdates = Userdata.select()

    for userdate in userdates:
        print(userdate.name, userdate.age)


if __name__ == "__main__":
    display_all_userdata()
