#Max Louis
#Development Iteration task 2
#16/10/14

column = int(input("Enter the number of colums:")) + 1
row = int(input("Enter the number of rows"))
originalColumn = column

for rows in range(row):
    for columns in range(1,column):
        print("*",end="")
        column -= 1
        if column == 1:
            column = originalColumn
            print("\n")
