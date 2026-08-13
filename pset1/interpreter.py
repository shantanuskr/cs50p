k = input("Expression: ")
x, y, z = k.split()


if y == '+':
    m = int(x) + int(z)
    print(f"{m:.1f}")
elif y == '-':
    m = int(x) - int(z)
    print(f"{m:.1f}")
elif y == '*':
    m = int(x) * int(z)
    print(f"{m:.1f}")
else:
     m = int(x) / int(z)
     print(f"{m:.1f}")

