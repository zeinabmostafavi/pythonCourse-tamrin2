number1 = int(input("\nplease Enter first Number: "))
number2 = int(input("please Enter second Number: "))

b_m_m = 0

max = max(number1, number2)
min = min(number1, number2)

for i in range(1, max):
    if max % i == 0:
        if min % i == 0:
            if i > b_m_m:
                b_m_m = i

print("b.m.m: ", b_m_m)
