def calculateAbsolute():  
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))       
    if in_num > 21:
        difference = abs((in_num - 21)*2)
    else:
        difference = abs(in_num - 21)
    print("Result: " + str(difference))
    # end assignment-10
## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
