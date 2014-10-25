#Max Louis
#S&C Task 2
#23/10/14
import time

denary = int(input("Please enter a number from 0, up to 255"))

loop = True

while loop == True:
    if (denary > 0 and denary < 256) != True:
        print("Please enter a value within the boundary.")
        time.sleep(1)
        loop = True
        break

    #Variables for each placeholder
    bit8 = 128
    bit7 = 64
    bit6 = 32
    bit5 = 16
    bit4 = 8
    bit3 = 4
    bit2 = 2
    bit1 = 1
    current = denary
    #Decisions
    #1
    if denary >= bit1:
        current -= bit1
        bit1 = 1
    else:
        bit1 = 0
        
    #2
    if denary >= bit2:
        current -= bit2
        bit2 = 1
    else:
        bit2 = 0
      
    #3
    if denary >= bit3:
        current -= bit3
        bit3 = 1
    else:
        bit3 = 0
    
    #4
    if denary >= bit4:
        current -= bit4
        bit4 = 1
    else:
        bit4 = 0  
      
    #5
    if denary >= bit5:
        current -= bit5
        bit5 = 1
    else:
        bit5 = 0
      
    #6
    if denary >= bit6:
        current -= bit6
        bit6 = 1
    else:
        bit6 = 0

    #7
    if denary >= bit7:
        current -= bit7
        bit7 = 1
    else:
        bit7 = 0
        
    #8
    if denary >= bit8:
        current -= bit8
        bit8 = 1
    else:
        bit8 = 0
        

        
    

    print("The 8-bit binary equivalent of {0} is: {1}{2}{3}{4}{5}{6}{7}{8}".format(denary,bit8,bit7,bit6,bit5,bit4,bit3,bit2,bit1))
    loop = False


   
