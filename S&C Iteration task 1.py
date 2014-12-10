#Max Louis
#S&C Iteration task 1
#16/10/14 - 10/11/14 modification

number = int(input("Enter a number:"))

for repeat in range(1,number+1):
    print("{0:> 3} ".format(repeat ** 2),end="")
    if repeat % 5 == 0:
        print("\n")
