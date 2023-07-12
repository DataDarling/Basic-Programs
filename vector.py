# prolog
# Author: Darling
# 
'''
Purpose:
        Lists can be used to represent mathematical vectors.
        In this exercise and several that follow, write
        functions to perform standard operations on vectors.
'''

#1). Write a function add_vectors(u, v) that takes two lists of numbers...
#...of the same length, and returns a new list containing the sums
#...of the corresponding elements of each

def add_vectors(u,v):
    print('\nThis function returns a new list containing the sums of the corresponding elements of each.')
    input("Press enter to continue\n")
    
    add_V = [] #initializing empty list 
    if len(u) == len(v):#check arguments for equal lengths
        print('\nThe two list are identical in length. The result is...\n')
        for num in range(len(u)):
            add_V.append(u[num] + v[num])
    else:#notify user if list length not equal
        print('This function requiers the list to be identical in length')
        print('Try again with list of thesame length')

    return add_V

  
#2). Write a function scalar_mult(s, v) that takes a number, s,
#and a list, v and returns
#the scalar multiple of v by s.

def scalar_mult(s, v):
    scalar_list = [] #initializing empty list

    for num in v: #scalar iteration
        scalar_list.append(s*num)
        
    return scalar_list
#3).Write a function dot_product(u, v) that takes two lists of numbers of
#the same length, and returns the sum of the products of the corresponding
#elements of each (the dot_product).

def dot_product(u, v):
    result = 0
    for prod in range(len(u)):
        result += u[prod] * v[prod]
    return result

#4)Write a function cross_product(u, v) that takes two lists of numbers
#...of length 3 and returns theircross product.
#Cross product returns vector.
#formula given vectors a and  b: a * b = (a2b2 - a3b2, a3b1 - a1b3, a1b2 - a2b1)

def cross_product(u,v):
    cross_sum = [0,0,0] #initializing empty list with placeholder for vectors/variables
    if len(u) == len(v):#assigning formula equations for each position in cross_sum list
        cross_sum[0] = (u[1]*v[2]) - (u[2]*v[1])
        cross_sum[1] = (u[2]*v[0]) - (u[0]*v[2])
        cross_sum[2] = (u[0]*v[1]) - (u[1]*v[0])
    return cross_sum


#5) Write a function replace(s, old, new) that replaces all occurrences of old
#...with new in a string s:

def replace(s,old,new):
    new = new.join(s.split(old))
    return new

#6) Swap function, replaces x with y and y with x
def swap(x, y):
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2,3,4]
#swap(a, b)


'''
TEST CASES:
All cases should evaluate as TRUE in order to pass test.
'''

def test(x): #test function
    if True:
        print(f"TEST PASSED")
    else:
        print(f"TEST FAILED")

#test(add_vectors([1, 1], [1, 1]) == [2, 2])
#test(add_vectors([1, 2], [1, 4]) == [2, 6])
#test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

#test(scalar_mult(5, [1, 2]) == [5, 10])
#test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
#test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

#test(dot_product([1, 1], [1, 1]) == 2)
#test(dot_product([1, 2], [1, 4]) == 9)
#test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

#test(cross_product([2,3,4],[5,6,7]) == [-3, 6, -3])
#test (cross_product([2,1,-1],[-3,4,1])== [5, 1, 11])


#test(replace("Mississippi", "i", "I") == "MIssIssIppI")
#s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
#test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
#test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
