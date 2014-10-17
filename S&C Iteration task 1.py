#Max Louis
#S&C Iteration task 1
#16/10/14

number = int(input("Enter a number:"))

for repeat in range(1,number+1):
    print("{0:> 3} ".format(repeat ** 2),end="")
    if repeat % 5 == 0:
        print("\n")
