from db_config import Userdata


def read_alldata():
    userdates = Userdata.select()
    for userdate in userdates:
        print(f"Name: {userdate.name} Age: {userdate.age}")


if __name__ == "__main__":
    read_alldata()
