from io import open_code


with open("OpeningAFile/welcome.txt", "r") as file:
    for i in file.readlines():
        print(i)