
second = int(input("Enter Number1: "))

if second < 0:
    print("error")
else:
    hour = int(second/3600)
    second = second-(hour*3600)
    print("second:", second)
    minute = int(second/60)
    second = second-(minute*60)

    print(hour, ":", minute, ":", second)
