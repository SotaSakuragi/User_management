from db_config import Userdata


def create_userdata():
    # インスタンスを生成してから保存
    message = Userdata(name="Bob", age=20)
    message.save()  # 保存
    # インスタンスを生成しないで保存
    Userdata.create(name="Tom", age=18)


if __name__ == "__main__":
    create_userdata()
