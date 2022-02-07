import random

if __name__ == "__main__":
    counter = 0
    pass_list = []
    for i in range(40):
        good_pass = 0
        passw = ""
        for i in range(12):
            val = random.randint(33, 126)
            passw += chr(val)

        mini_rockyou = open("minirockyou.txt", "r")
        lines = mini_rockyou.readlines()

        for line in lines:
            if passw != line:
                continue
            elif passw == line:
                good_pass = 1

        if good_pass == 0:
            pass_list.append(passw)

        elif good_pass == 1:
            continue

    print(pass_list)
