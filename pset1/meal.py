def main():
    tm = input("Waht time is it? ")
    a = convert(tm)
    if a >= 7.0 and a <= 8.0:
        print("breakfast time")
    elif a>=12.0 and a <= 13.0:
        print("lunch time")
    elif a >= 18.0 and a <= 19.0:
        print("dinner time")
    else:
        exit()


def convert(time):

    x, z = time.split(":")
    k = int(x)
    l = int(z)
    l = float(l/60)

    return  k + l


if __name__ == "__main__":
    main()
