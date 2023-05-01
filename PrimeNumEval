# Prolog
# Author: Darling Ngoh
'''
 Purpose:
    This program prompts the user to enter a number then displays a message indicating
    whether the number is prime, not prime or negative
'''
import math
#1st function is main function which gets user input and calls prime function 

#define main function
def main ():
    print("      *** isPrime ***\n")
    #get user input
    num = int(input("Please provide an integer: "))
    #call prime function
    is_prime(num)

#2nd function is prime function which is refrenced by main function intended to
#...evaluate whether a number is prime, not prime, or negative

#def prime function
def is_prime(value):
    status = False
    #conditional and boolean operators to evaluate whether number is prime, not prime
    if value == 0 or value == 1:
        status = False

    elif value > 1: 
        for x in range (2,int(math.sqrt(value))+1): #range from [2,sqrt num]
            if (value % x) == 0: #check for factors
                break
        else:
            status = True

    #printing results
    if status:
        print(f"The integer {value} is prime.")
    else:
        if value < 0: #identifying negative num
            print(f"The integer {value} is negative.")
        else:
            print(f"The integer {value} is not prime.")


main()
