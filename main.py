num = int(input("mul: "))
factors = []
for i in range(1, num+1):
    if num%i==0:
        factors.append(i)

print(factors)

add = int(input("add: "))
for number in factors:
    for adder in factors:
        if (number+adder==add or number-adder== add) and (number*adder == num ):
            print(number, adder)