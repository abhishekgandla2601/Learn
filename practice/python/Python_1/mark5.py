while (True):
    print('Which operation do you want to perform:')
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.Exit")
    c = int(input("Choose the operation you want to perform:"))

    if c == 5:
        
        print('Do you want to exit?')
        
        choice = input('If Yes, Enter "Y" or Else if you want to continue Enter "N" :')
        
        
        if choice == "Y":
            exit()
        else:
            continue
          
    a1 = int(input('Enter Your 1st number:'))
    a2 = int(input('Enter Your 2nd number:'))
    if c == 1:
        print("You have choosen Addition operation")
        
        print(a1,"+",a2, '=', a1+a2)
        

    elif c== 2:
        print("You have choosen Subtraction operation")
        
        print(a1,"-",a2, '=', a1-a2)

    elif c == 3:
        print("You have choosen Multiplication operation")
        
        print(a1,"*",a2, '=', a1*a2)

    elif c == 4:
        print("You have choosen Division operation")
        
        print(a1,"/",a2, '=', a1/a2)

    # incomplete program