def main():
    strin = convert()
    print(strin)

def convert():
    str = input()
    return str.replace(":)","🙂").replace(":(", "🙁")

main()