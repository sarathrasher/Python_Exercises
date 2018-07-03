factors = []
num = int(raw_input("Choose a number. \n"))

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
    
print factors