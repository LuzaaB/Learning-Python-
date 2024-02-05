money = float(input("Enter initial amount : "))
time = int(input("Enter time : "))
rate = float(input("Enter rate : "))
len = time+1

total:float = money*rate**((time)-1)
print(total)



# print(0.01*2**29)