list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]


while True:
    try:
        date = input("Date: ").strip()
        if '/' in date:
            mm, dd, yyyy = date.split('/')
            d = int(dd)
            m = int(mm)
            if mm.isdigit() and 1<=d<=31 and 1<=m<=12:
                print(f"{yyyy}-{m:02}-{d:02}")
                break

        elif ',' in date:
            x, yyyy = date.split(',')
            mm, dd = x.split(' ')
            d = int(dd)
            if mm.isalpha() and 1<=d<=31:
                for month in range(len(list)):
                    if mm == list[month]:
                        print(f"{yyyy}-{month+1:02}-{d:02}")
                        exit()
    except ValueError:
        date = input("Date: ").strip()
