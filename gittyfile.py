def input_num():
    global number1
    number1 = int(input("Please enter a number: "))
    
    ''' This function allows the user to input the required number.'''
def evenodd():
    if number1 % 2 == 0: #Checks if the number is even or odd
        print("The number is even") #Confirms the number is even
    else:
        print("The number is odd") #Confirms the number is odd
def expo():
    sqnumber1 = number1**2 #Calculates the exponential 2
    cbnumber1 = number1**3 #Calculates the exponential 3        
    print("The square is",sqnumber1)
    print("The cube is",cbnumber1)
def main():
    input_num()
    evenodd()
    expo()
main()