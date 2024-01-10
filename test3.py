numm = 1
c = 0
d = {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
a = [[0] * 6 for i in range(7)]


def check_diag(a):
    pass


def check_vert(a):
    l = [0, 0]
    for listt in a:
        check = 0
        for i in range(len(listt) - 1):
            if check == 2:
                if numm == 1:
                    return [1, 2]
                else:
                    return [1, 1]
            if listt[i] != 0 and listt[i] == listt[i + 1]:
                check += 1
            else:
                check = 0
    return l


def check_hor(a):
    a = rot(a)
    l = [0, 0]
    for listt in a:
        check = 0
        for i in range(len(listt) - 1):
            if check == 3:
                if numm == 1:
                    return [1, 2]
                else:
                    return [1, 1]
            if listt[i] != 0 and listt[i] == listt[i + 1]:
                check += 1
            else:
                check = 0
    return l


def writ(num):
    y = int(input()) - 1
    if y >= 7:
        print("неккоректный ввод")
        writ(num)
    else:
        if d[y] >= -6:
            d[y] -= 1
            a[-y - 1][d[y] + 1] = num
            if num == 1:
                num = 2
            else:
                num = 1
            return num
        else:
            print("неккоректный ввод")
            writ(num)
    if num == 1:
        num = 2
    else:
        num = 1
    return num


def rot(a):
    return list(zip(*a[::-1]))


while not (check_hor(a)[0]) and not (check_vert(a)[0]) and c != 42:
    numm = writ(numm)
    for i in rot(a):
        print(*i)
    c += 1
    if check_hor(a)[0]:
        print(f"выиграл:{check_hor(a)[1]}")
    elif check_vert(a)[1]:
        print(f"выиграл:{check_vert(a)[1]}")
