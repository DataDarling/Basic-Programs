#Think Like A Data Scientist- TLADS - Chapter 7: Iteration Excersises

'''
These excercises go over some basic concepts of iteration.
Computers are often used to automate repetitive tasks. Repeating identical or similar tasks
without making errors is something that computers do well and people do poorly.
Repeated execution of a set of statements is called iteration.

Concepts covered:
The while statement,Composition of list traversal, summing, counting, testing conditions and early exit 

Glossary:
1. Write a function to count how many odd numbers are in a list.

2. Sum up all the even numbers in a list.

3. Sum up all the negative numbers in a list.

4. Count how many words in a list have length 5.

5. Sum all the elements in a list up to but not including the first even number. (Write your
unit tests. What if there is no even number?)

6. Count how many words occur in a list up to and including the first occurrence of the word
“sam”. (Write your unit tests for this case too. What if “sam” does not occur?)

7. Add a print function to Newton’s sqrt function that prints out better each time it is
calculated. Call your modified function with 25 as an argument and record the results.

8. Trace the execution of the last version of print_mult_table and figure out how it
works.

9. Write a function print_triangular_numbers(n) that prints out the first n tri-
angular numbers. A call to print_triangular_numbers(5) would produce the

following output:
1 1
2 3
3 6
4 10
5 15
(hint: use a web search to find out what a triangular number is.)

10. Write a function, is_prime, which takes a single integer argument and returns True
when the argument is a prime number and False otherwise. Add tests for cases like
this:
test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))

11. Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk
pirate makes a turn, and then takes some steps forward, and repeats this. Our social
science student now records pairs of data: the angle of each turn, and the number of
steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43,
12)]. Use a turtle to draw the path taken by our drunk friend.

12. Set up a list of pairs so that the turtle draws a house with a
cross through the centre, as show here. This should be done without going over any of
the lines / edges more than once, and without lifting your pen.

15. Write a function num_even_digits(n) that counts the number of even digits in n.
These tests should pass:
test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)

16. Write a function sum_of_squares(xs) that computes the sum of the squares of the
numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return
4+9+16 which is 29:
test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)

17. You and your friend are in a team to write a two-player game, human against computer,
such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play one
round of the game, while you will write the logic to allow many rounds of play, keep
score, decide who plays, first, etc. The two of you negotiate on how the two parts of
the program will fit together, and you come up with this simple scaffolding (which your
friend will improve later):

(a) Write the main program which repeatedly calls this function to play the game, and
after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
It then asks the player “Do you want to play again?” and either plays
again, or says “Goodbye”, and terminates.

(b) Keep score of how many wins each player has had, and how many draws there have
been. After each round of play, also announce the scores.

(c) Add logic so that the players take turns to play first.

(d) Compute the percentage of wins for the human, out of all games played. Also
announce this at the end of each round.

(e) Draw a flowchart of your logic.
'''
import sys

import turtle #examples starting at ex. 11
my_turtle = turtle



li = [1,3,-2,5,10,-1,-4, 8] #integer list
wo = ["hi", "you are awesome", "world","sam", "five", "eleven", "turtles"] #word list

#1. Write a function to count how many odd numbers are in a list.
def odd_num(givenList):
    print(givenList)
    count = 0
    for num in givenList:
        if num % 2 != 0:
            count += 1
    print ("\nThere are {0} odd numbers in the list\n".format(count))
    return(count)
    
#odd_num(li)

#2:  Sum up all the even numbers in a list.
def even_sum(givenList):
    print(givenList)
    sum_even = 0
    for num in givenList:
        if num % 2 == 0:
            sum_even += num
    print ("\nThe sum of all even numbers in the list is: ", sum_even)
    return(sum_even)

#even_sum(li)

#3. Sum up all the negative numbers in a list.
def negative_sum(givenList):
    print(givenList)
    sum_negative = 0
    for num in givenList:
        if num < 0:
            sum_negative += num
    print("\nThe sum totall of all negative numbers are: ", sum_negative)
    return(sum_negative)

#negative_sum(li)

#4. Count how many words in a list have length 5.
def word_count(givenList):
    print(givenList)
    word_len_5 = 0
    for word in givenList:
        if len(word) == 5:
            word_len_5 += 1
        else:
            continue
    print("\nThe sum totall of all words with character length 5: ", word_len_5, "\n")
    
#word_count(wo)   

#5. Sum all the elements in a list up to but not including the first even number. (Write your
#unit tests. What if there is no even number?)
def sum_til_even(givenList):
    print(givenList)
    sum_till = 0
    for num in givenList:
        print(num)
        if num % 2 != 0:
            sum_till += num
        else:
            break
    print("\nThe sum of elements in list but not including the first even number: ", sum_till, "\n")
#sum_til_even(li)

#6. Count how many words occur in a list up to and including the first occurrence of the word
#“sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
def count_til_sam(givenList):
    print(givenList)
    count_till = 0
    for words in givenList:
        print(words)
        if words != "sam":
            count_till += 1
        else:
            count_till += 1
            break
    print("\nThe count of words in list up to and including the first occurence of word 'sam': ", count_till, "\n")
    
#count_til_sam(wo)

#7. Add a print function to Newton’s sqrt function that prints out better each time it is
#calculated. Call your modified function with 25 as an argument and record the results.
def newton_sqrt(givenNum):
    aprox_sqrt = givenNum/2.0
    while True:
        better = (aprox_sqrt + givenNum/aprox_sqrt)/2.0
        if abs(aprox_sqrt - better) < 0.001:
            return better
        aprox_sqrt = better

#print(newton_sqrt(5))
        
#9. Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
'''A triangular number is a count of the objects arranged in an equilaterall triangle
'''
def triangular_nums(num):
    triangular_count = 0
    for number in range(num):
        if number > 0:
            triangular_count = (number*(number + 1))//2
            print("The number of sides: {0}\t The number of objects: {1}".format(number, triangular_count))
        else:
            continue
#triangular_nums()

#10. Write a function, is_prime, which takes a single integer argument and returns True
#...when the argument is a prime number and False otherwise. Add tests for cases like
def is_prime(num):
    prime_nums = [2,3]
    for i in range (1,num):
        prime_nums.append(6*i - 1) #formula for prime numbers (interistingly some numbers are not prime) for the sake of syntax this will be allowed.
        prime_nums.append(6*i + 1) #formula for prime numbers
    
    if num in prime_nums:
        return True
    else:
        return False
#is_prime(2)
'''
#11. Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk
pirate makes a turn, and then takes some steps forward, and repeats this. Our social
science student now records pairs of data: the angle of each turn, and the number of
steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43,
12)]. Use a turtle to draw the path taken by our drunk friend.
'''
def drunk_pirate():
    experimental_data = [(160, 20), (-43, 10), (270, 8), (-43,12)]
    for i,e in experimental_data:
        my_turtle.right(i)
        my_turtle.forward(e)
#drunk_pirate()
'''
#12. Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did
#above, where the first item of the pair is the angle to turn, and the second item is the
#distance to move forward. Set up a list of pairs so that the turtle draws a house with a
#cross through the centre, as show here. This should be done without going over any of
#the lines / edges more than once, and without lifting your pen.
house_data = [(0, 50), (-90, 50), (-45, 35), (-90,35), (-45,50), (-135,70), (-135,50), (-135,70) ]
'''
def house():
    for i,e in house_data:
        my_turtle.right(i)
        my_turtle.forward(e)
#house()

#15. Write a function num_even_digits(n) that counts the number of even digits in n.
def num_even_digits(n):
    count = 0
    for num in n:
        if num % 2 == 0:
            count += 1
        else:
            continue
    print("There are {0} even digits in the list.".format(count))

#num_even_digits(li)

'''
#16. Write a function sum_of_squares(xs) that computes the sum of the squares of the
#numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return
#4+9+16 which is 29:
'''
ei = [2,3,4]
def sum_square(n):
    square_sum = 0
    for num in n:
        square_sum += num**2
    return(square_sum)

#sum_square(ei)
#-----------------------------------------------------------------------------------------------------------------
'''
#17.
(a) Write the main program which repeatedly calls this function to play the game, and
after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
It then asks the player “Do you want to play again?” and either plays
again, or says “Goodbye”, and terminates.

(b) Keep score of how many wins each player has had, and how many draws there have
been. After each round of play, also announce the scores.

(c) Add logic so that the players take turns to play first.

(d) Compute the percentage of wins for the human, out of all games played. Also
announce this at the end of each round.

(e) Draw a flowchart of your logic.
'''
#your friend will complete this function
def play_once():
    '''
The human gets to play first, else the
computer gets to play first. When the round ends,
the return value of the function is one of
-1 (human wins), 0 (game drawn), 1 (computer wins).
    '''
    # This is all dummy scaffolding code right at the moment...
    import random
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    who_goes_first = result

    if who_goes_first == -1:
        print("Human plays first={0}, winner={1} ".format(who_goes_first, result))
        
    elif who_goes_first == 1:
        print("Computer plays first={0}, winner={1} ".format(who_goes_first, result))
    else:
        print("Human plays first={0}, winner={1} ".format(who_goes_first, result))
    
    return result

def play_again(): #funtion that calls to play game repeatedly
    human_score = 0
    computer_score = 0
    draws = 0
    totall_games = 0
    #human_percentage = (human_score//totall_games)*100
    #computer_percentage = (computer_score/totall_games)*100
    user_input = input("Would you like to play game? y or n\n ")
    while user_input == "y":
        result = play_once()
        totall_games += 1
        if result == 1:
            computer_score += 1
            print("Computer Wins\n")
            print("Totall games:{3}\t Human Score:{0}\tComputer Score:{1}\tDraw(s):{2}\n".format(human_score,computer_score,draws,totall_games))
            print("Percentage of wins*\n " + "Human: " + str((human_score/totall_games)*100)[:3] + "% ", " Computer: " + str((computer_score/totall_games)*100)[:3]+ "%\n\n") #need to work on this
            input("press enter to continue......")
        elif result == -1:
            human_score += 1
            print("Human Wins\n")
            print("Totall games:{3}\t Human Score:{0}\tComputer Score:{1}\tDraw(s):{2}\n".format(human_score,computer_score,draws,totall_games))
            print("Percentage of wins*\n " + "Human: " + str((human_score/totall_games)*100)[:3] + "% ", " Computer: " + str((computer_score/totall_games)*100)[:3]+ "%\n\n")
            input("press enter to continue......")

        else:
            draws += 1
            print("Game Drawn\n")
            print("Totall games:{3}\t Human Score:{0}\tComputer Score:{1}\tDraw(s):{2}\n".format(human_score,computer_score,draws,totall_games))
            print("Percentage of wins*\n " + "Human: " + str((human_score/totall_games)*100)[:3] + "% ", " Computer: " + str((computer_score/totall_games)*100)[:3]+ "%\n\n")
            input("press enter to continue......")

        #print("Percentage of wins...\n " + "Human: " + str((human_score//totall_games)*100) + "% "+ " Computer: " + str((computer_score//totall_games)*100)+"%\n\n")

        while True: #looping sequence to only allow user input of y or n, otherwise user is promted to answer again until conditions are met
            user_continue = input("Would you like to continue game? y or n\n ")
            if user_continue == "y":
                break
            if user_continue == "n":
                break
            else:
                print("Invalid input... either press n = to exit or y = continue\n")
                continue
        if user_continue == "n":
            break
    print("Thanks for playing GOODBYE")
#play_again()


#-----------------------------------------------------------------------------------------------------------------

#test funtion
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
        print(msg)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)


#add tests like these to the test suite whenever possible
""" don't forget to use return function to ensure the test can run successfully given it's a fruitful function
and not a void funtion.
"""
def test_suite():
    test(sum_square([2,3,4]) == 29)
    test(sum_square([]) == 0)
    test(sum_square([2,-3,4]) == 29)
    

#test_suite()
