#Going through Basic String Excercises
'''
These excercises cover...
- indexing ([]) Access a single character in a string using its position (starting from 0). 

- length function (len) Returns the number of characters in a string.

- for loop traversal (for) Traversing a string means accessing each character in the string, one
at a time. 

- slicing ([:]) A slice is a substring of a string. Example: ’bananas and cream’[3:6]
evaluates to ana (so does ’bananas and cream’[1:4]).

- string comparison (>, <, >=, <=, ==, !=) The six common comparison operators
work with strings, evaluating according to lexicographical order. Examples: "apple"
< "banana" evaluates to True. "Zeta" < "Appricot" evaluates to False.

- in and not in operator (in, not in) The in operator tests for membership. In the case
of strings, it tests whether one string is contained inside another string. Examples:
"heck" in "I’ll be checking for you." evaluates to True. "cheese"
in "I’ll be checking for you." evaluates to False.
'''
'''
Glossary:

#2. Modify:
-----------------------------
prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    print(letter + suffix)
 ----------------------------       
so that Ouack and Quack are spelled correctly.

#3. Encapsulate
---------------------------------
fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)
---------------------------------
in a function named count_letters, and generalize it so that it accepts the string and
the letter as arguments. Make the function return the number of characters, rather than
print the answer. The caller should do the printing.

#4. Now rewrite the count_letters function so that instead of traversing the string, it
repeatedly calls the find method, with the optional third parameter to locate new occur-
rences of the letter being counted.

#5. Assign to a variable in your program a triple-quoted string that contains your favourite
paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspira-
tional verses, etc.
Write a function which removes all punctuation from the string, breaks the string into
a list of words, and counts the number of words in your text that contain the letter “e”.
Your program should print an analysis of the text like this:
Your text contains 243 words, of which 109 (44.8%) contain an "e".

6. Print out a neatly formatted multiplication table, up to 12 x 12.

7. Write a function that reverses its string argument, and satisfies these tests:
test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")

8. Write a function that mirrors its argument:
test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")

9. Write a function that removes all occurrences of a given letter from a string:
test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") = "")
test(remove_letter("b", "c") = "c")

10. Write a function that recognizes palindromes. (Hint: use your reverse function to
make this easy!):
test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome("")) # Is an empty string a palindrome?

11. Write a function that counts how many times a substring occurs in a string:
test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 2)

12. Write a function that removes the first occurrence of a string from another string:
test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")

13. Write a function that removes all occurrences of a string from another string:
test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
'''
import sys

'''
#2. Modify: so that Ouack and Quack are spelled correctly.
'''
def spelled_correctly():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == "Q" or letter == "O":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)
#spelled_correctly()
'''
#3. Encapsulate: in a function named count_letters, and generalize it so that it accepts the string and
the letter as arguments. Make the function return the number of characters, rather than
print the answer. The caller should do the printing.
'''
def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return(count)

#print(count_letters("my name is abcdefg", " "))
'''
#4. Now rewrite the count_letters function so that instead of traversing the string, it
repeatedly calls the find method, with the optional third parameter to locate new occur-
rences of the letter being counted.
'''
def count_letters_updated(string, letter, start=0): #the basic logic, although alot more could be expounded on given the exercise
    return(string[start:].find(letter))

#print(count_letters_updated("darlingisgreat", "a", ))

'''
#5. Assign to a variable in your program a triple-quoted string that contains your favourite
paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspira-
tional verses, etc.
Write a function which removes all punctuation from the string, breaks the string into
a list of words, and counts the number of words in your text that contain the letter “e”.
Your program should print an analysis of the text like this:
Your text contains 243 words, of which 109 (44.8%) contain an "e".
'''

#initializing variable entailing poem by Rumi
rumi_poem = '''
All through eternity
Beauty unveils His exquisite form
in the solitude of nothingness;
He holds a mirror to His Face
and beholds His own beauty.
he is the knower and the known,
the seer and the seen;
No eye but His own
has ever looked upon this Universe.

His every quality finds an expression:
Eternity becomes the verdant field of Time and Space;
Love, the life-giving garden of this world.
Every branch and leaf and fruit
Reveals an aspect of His perfection-
They cypress give hint of His majesty,
The rose gives tidings of His beauty.

Whenever Beauty looks,
Love is also there;
Whenever beauty shows a rosy cheek
Love lights Her fire from that flame.
When beauty dwells in the dark folds of night
Love comes and finds a heart
entangled in tresses.
Beauty and Love are as body and soul.
Beauty is the mine, Love is the diamond.

They have together
since the beginning of time-
Side by side, step by step.
'''


#initializing punctuations
punctuation = '''!\#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~'''

#remove punctuations in string using loop + punctuation string
def remove_punct(s):
    count = 0 #initializing variable to keep track of words with letter "e"
    for word in s:
        if word in punctuation:
            s = s.replace(word,"")
            
    joint_poem = s.split() #initializing transleted poem as list
    
    for word in joint_poem: #looping through poem list to count number of occurences of letter "e"
        if "e" in word:
            count += 1
            
    letter_perc = count/len(joint_poem)*100 #initializing percentage of letters
    
    print("Your text contains {0} words, of which {1} ({2}%) contain an 'e'".format(len(joint_poem),count,round(letter_perc,2)))
    print("\n\n")
    print(s)                                                        

#remove_punct(rumi_poem)
'''
#6. Print out a neatly formatted multiplication table, up to 12 x 12.
'''
def multi_table():
    layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>13}{6:>13}{7:>13}{8:>13}{9:>13}{10:>13}{11:>13}" #initializing layout for multiplication table > is amount of right center
    print(layout.format("i**1","i**2","i**3","i**4","i**5","i**6","i**7","i**8","i**9","i**10","i**11","i**12"))

    for i in range(1,13): #starts at 1 and loops up till but not including 13
        print(layout.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))

#multi_table()
'''
#7. Write a function that reverses its string argument, and satisfies these tests:
test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
'''
def reverse(word):
    return(word[::-1])

#print(reverse("happy"))

'''
#8. Write a function that mirrors its argument:
test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")
'''
def mirror(word):
    return(word + word[::-1])

#print(mirror("happy"))

'''
9. Write a function that removes all occurrences of a given letter from a string:
test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") = "")
test(remove_letter("b", "c") = "c")
'''
def remove_letter(letter,word):
    new_word = ""
    for i in word:
        if letter == i:
            continue
        else:
            new_word += i
    return(new_word)
            
#print(remove_letter("a", "happy"))

'''
#10. Write a function that recognizes palindromes. (Hint: use your reverse function to
make this easy!):

Definition- Palindrome is a word, prase or sequence that reads the same backwards as forward

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome("")) # Is an empty string a palindrome?
'''
def is_palindrome(word):
    if reverse(word) == word:
        return True
    else:
        return False

#print(is_palindrome("madam"))

'''
#11. Write a function that counts how many times a substring occurs in a string:
test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 2)
'''
def count(substr,word):
    count = word.count(substr)  
    return count

#print(count("is", "Mississippi"))
'''
#12. Write a function that removes the first occurrence of a string from another string:
test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
'''
def remove(firstStr,word):
    new_str = word.replace(firstStr,"",1) #replacing occurences of first string with empty backets
    return(new_str)

#print(remove("a","banana"))

'''
13. Write a function that removes all occurrences of a string from another string:
test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
'''
def remove_all(substr, word):
    new_str = word.replace(substr,"") #thesame concept as excercise #12 although the delimeter for the amount of replacement occurences is omitted leading to ALL occurences being replaced by default
    return (new_str)

#print(remove_all("an","anple")) #be sure to remove "print" statement before testing
#-----------------------------------------------------------------------------------------------------------------

#test funtion
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} PASSED.".format(linenum)
        print(msg)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)


#add tests like these to the test suite whenever possible
""" don't forget to use return statement to ensure the test can run successfully given it's a fruitful function
and not a void funtion.
"""
def test_suite():
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")
    

#test_suite()
