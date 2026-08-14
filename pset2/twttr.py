str = input("Input: ")

for char in str:

    match char:
        case "a" | "A":
            str = str.replace(char, "")

        case "e" | "E":
            str = str.replace(char, "")

        case "i" | "I":
            str = str.replace(char, "")

        case "o" | "O":
            str = str.replace(char, "")

        case "u" | "U":
            str = str.replace(char, "")

print(str)

