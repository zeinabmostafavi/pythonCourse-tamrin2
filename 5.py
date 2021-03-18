while True:
    h = int(input("Enter hours: "))
    m = int(input("Enter minutes: "))
    s = int(input("Enter seconds: "))
    if h < 0 or m < 0 or m > 60 or s < 0 or s > 60:
        print("error")
    else:
        print("you Enter:", h, ":", m, ":", s)
        time = (h * 3600) + (m * 60) + s
        print("second: ", time)
        message = input("you want exit(N/Y): ")
        if message == "y" or message == "Y" or message == "Yes" or message == "yes":
            exit()
