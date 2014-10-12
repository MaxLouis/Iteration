password = input("Please enter your password")
repeat = True
while repeat != False:
    if password == "secret":
        print("Correct")
        repeat = False

    else:
        for repeat in range(0,2):
            print(False)
            repeat = True
