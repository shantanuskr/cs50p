x = 50

def main():

    print(f"Amount Due: {x}")

    for i in range(50):
        y = int(input("Insert Coin: "))
        if y == 25:
            remain(y)
        elif y == 10:
            remain(y)
        elif y == 5:
            remain(y)
        else:
            remain(0)


def remain(k):
    for i in range(50):
        global x
        x = x - k
        if x > 0:
            print(f"Amount Due: {x}")
            break
        elif x == 0:
            print(f"Change Owed: {x}")
            exit()
        else:
            x = -x
            print(f"Change Owed: {x}")
            exit()
    return
main()
