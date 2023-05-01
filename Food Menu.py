# Prolog
# Author: Darling Ngoh
'''
 Purpose:
    This program will present menu choices from a restaurant to a customer, and calculate
    the bill (total of the prices of the items they chose)
'''
#initializing main function
def main():
    #initializing total bill variable
    total_bill = 0
    #initializing menu variable assinging to dictionary
    menu_items = {"Grilled Cheese":7,"Nachos":5,"Chicken":8,"Hamburger":8,"Cheeseburger":10,"Hot Dog":6}

    #calculating sales tax 
    tax = 20/100

    #printing out initial instructions to user
    print("Welcome to Dairy King! Please enter y or n for your menu selections.")

    #structuring out bookean values to control flow of questions and tally in total bill
    input1 = input("Do you want a grilled cheese sandwich? ")
    if input1 == "y":
        total_bill += menu_items["Grilled Cheese"]
    input2 = input("Do you want a serving of nachos? ")
    if input2 == "y":
        total_bill += menu_items["Nachos"]
    input3 = input("Do you want a chicken sandwich? ")
    if input3 == "y":
        total_bill += menu_items["Chicken"]
    input4 = input("Do you want a Hamburger? ")
    if input4 == "y":
        input4_2 = input("Do you want cheese on that? ")
        if input4_2 == "y":
            total_bill += menu_items["Cheeseburger"]
        else:
            total_bill += menu_items["Hamburger"]
    input5 = input("Do you want a hot dog? ")
    if input5 == "y":
        total_bill += menu_items["Hot Dog"]

    #printing final output
    print("The total for your food is $"+ str(total_bill))
    print("The total with 20% tip is $"+ str(total_bill + total_bill*tax))
    print("Thank you for your business!")

main()


    
