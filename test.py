def checknum():
    try:
        test = int(input("type number: \n"))
    except ValueError:
        print("Not a number")
        checknum()
        
checknum()
