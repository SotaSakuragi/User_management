from db_config import Userdata
from data_condition import condition


def confirmation(user_name):
    userdatas = Userdata.select().where(Userdata.name == user_name)
    if userdatas.exists():
        for userdata in userdatas:
            print(f"Duplicated user name {user_name}")
            condition()
    else:
        return


if __name__ == "__main__":
    user_name = "田中"
    confirmation(user_name)
