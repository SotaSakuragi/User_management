from read_all import read_alldata
from create_date import create_data


def main():
    with open("welcome.txt", "r") as file:  # 最初の文字列をtextからprint
        content = file.read()
    print(content)
    condition()


def condition():  # 入力された文字列で場合分け
    while True:
        command = input("Your command > ")
        if command == "S" or command == "s":
            read_alldata()  # 全て表示
        elif command == "A" or command == "a":
            create_data()  # 新しく追加
        elif command == "Q" or command == "q":
            print("Bye!")
            return
        else:
            print(f"{command}: command not found")
        print()


if __name__ == "__main__":
    main()
