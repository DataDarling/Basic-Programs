#prolog
# Author: Darling Ngoh 
'''
Purpose:
    This is a roster management program for the Atlanta Braves(World series Champions)
    Each batter will have some stats that we can edit, add, or remove.
'''


import unittest

#defining function that returns the player key and value within dictionary
def lookup_player(dic,key):
    if key in dic:
        return(dic[key])
    else:
        return("N/A")
#defining function that adds player to the list or ads second listing if name already in dict
def add_player_to_dict (dic,key,value):
    if key in dic:
        key = key + "(2)"
        dic[key] = value
    else:
        dic[key] = value
    return dic
#defining function that deletes player from dict
def delete_in_dict(dic,key):
    if key in dic:
        dic.pop(key)
        return dic
    else:
        return dic
#defining main function which comprises bulk of the logic        
def main():

# initial roster
    brave_roster = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
  }

# your code here
    print("     *** Braves Stats ***    \n")
    print("Welcome to My Braves Stats! What can I do for you? \n")
    print("   1. Search for a player")
    print("   2. Add a new player")
    print("   3. Remove a player \n")

    #boolean to control flow of user input only between inputs 1-3
    while True:
        user_choice = int(input("please type your choice number: "))
        if 1 <= user_choice <= 3:
            break
        else:
            print("\nInvalid input, please type a choice number 1, 2, or 3\n")
            continue
    #setting conditional execution for choice 1
    if user_choice == 1:
        lookup_user = input("\nEnter the name of the player you want to look up: ")
        first_name = lookup_user.split()[0]
        
        if lookup_player(brave_roster,lookup_user) == "N/A":
            print("\nOOps looks like we don't have this player in our registry: " + lookup_user )
        else:
            print("\n" + "Here are " + first_name + "'s stats: " + lookup_player(brave_roster,lookup_user))
            print("\nThanks for using My Braves Stats.")
            
    #setting condintional execution for choice 2
    if user_choice == 2:
        add_user = input("\nEnter the name of the player you want to add: ")
        if add_user in brave_roster:
            print("\nLooks like we already have that player in our rigistry, here is the complete team roster: ")
            for key in brave_roster:
                print("\t" + key +" "+ brave_roster[key])
        else:
            add_value = input("\nPlease add " + add_user.split()[0] + "'s stats: ")
            add_player_to_dict (brave_roster,add_user,add_value)
            print("\nHere’s the complete team roster:")
            for key in brave_roster:
                print("\t" + key +" "+ brave_roster[key])
    #setting conditional execution for choice 3
    if user_choice == 3:
        delete_user = input("\nEnter the name of the player you want to remove: ")
        if delete_user in brave_roster:
            delete_in_dict(brave_roster,delete_user)
            print("\n"+ delete_user + " has been removed from the roster, here is the updated list: ")
            for key in brave_roster:
                print("\t" + key +" "+ brave_roster[key])
        else:
            print("\nUh typo? " + delete_user.split()[0] + " does not play for us:)")
    input()
    
# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_player_success(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = test_dict["Austin Riley"]
    expected = lookup_player(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_search_player_no_result(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = "N/A"
    expected = lookup_player(test_dict, "Ronald Acuna")
    self.assertEqual(actual, expected)

  def test_add_player_sucess(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266"
    }
    expected = add_player_to_dict(test_dict, "Ronald Acuna", "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266")

    self.assertEqual(actual, expected)

  def test_add_player_duplicate(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    actual = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273", "Austin Riley(2)": "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214"}
    expected = add_player_to_dict(test_dict, "Austin Riley", "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214")
    self.assertEqual(actual, expected)

  def test_delete_player_sucess(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = {}
    actual = delete_in_dict(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = test_dict
    actual = delete_in_dict(test_dict, "Shohei Ohtani")
    self.assertEqual(actual, expected)

#uncomment to run main program
main()
    
#uncomment to run tests
unittest.main()
