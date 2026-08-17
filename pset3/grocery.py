dic = {}

while True:
    try :
        item = input().upper()
    except EOFError:
        print()
        break

    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

for key in sorted(dic):
    print(dic[key], key)
