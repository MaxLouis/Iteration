#Max Louis
#S&C Iteration task 1
#16/10/14

column = int(input("Enter the number of colums:"))
row = int(input("Enter the number of rows"))
originalColumn = column

for columns in range(1,column+1):
    print("*",end="")
    column -= 1
    if column == 1:
        column = originalColumn
