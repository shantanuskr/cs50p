frac = input("Fraction :")

while True:
    if '/' in frac:
        x, y = frac.split("/")
        if x.isdigit() and y.isdigit() and int(x) <= int(y) and int(y) != 0 :
            k = (int(x)/int(y))*100
            if k <= 1:
                print("E")
                exit()
            elif k>= 99:
                print("F")
                exit()
            else:
                    print(f"{k:.0f}%")
                    exit()
        else:
             frac = input("Fraction :")
    else:
        frac = input("Fraction :")
