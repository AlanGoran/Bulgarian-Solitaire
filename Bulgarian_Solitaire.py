import os
import time
import random

def round_play(pile_list):
	"""	
	1. The list of pile numbers is inputted.
	2. Pile numbers are subtracted by one and the sum of the subtractions are appended in the same list.
	3. Returns the new list of pile numbers.
	"""
	for batch in range(len(pile_list)):
		pile_list[batch]= pile_list[batch]-1
	pile_list.append(len(pile_list))
	return pile_list

def delete_zeros(pile_list):
	"""	
	1. The list of pile numbers is inputted.
	2. The list is sorted and elements that equals to zero are removed.
	3. The list is returned without zeros.
	"""
	pile_list.sort(reverse=True)
	return [batch for batch in pile_list if batch != 0]

def printer(pile_list): 
	"""
	1. The list of pile numbers is inputted.
	2. Every element in the list is printed by a for loop .
	3. Returns nothing.
	"""
	for batch in pile_list:
		print(batch,end=" ")
	print("\n")

def cycle_estimation(list_of_all_pile_lists,pile_list):
	"""
	1. Two lists are inputted one of them is the list of all previous pile lists and the other one is the current pile list.
	2. The goal with this function is to determine whether the current list has been shown before or not. 
	3. If the pile list has been used before it returns a signal so the game stops.
	"""
	for previous_pile_list in list_of_all_pile_lists:
		if previous_pile_list == pile_list:
			return True

def game_run(pile_list):
	"""
	1. List of the pile numbers is coming in to this function.
	2. Almost the entire play of this game is done in this function, it prints out the lists after each round and estimates whether the player wins or loses.
	3. The function returns a string that tells the player about game status. 
	"""
	printer(pile_list)
	list_of_all_pile_lists=[]
	for stage in range(25):
		list_of_all_pile_lists.append(delete_zeros(pile_list))
		list_of_previous_new_pile_lists=[delete_zeros(pile_list)]
		pile_list= delete_zeros(round_play(pile_list))
		list_of_previous_new_pile_lists.append(pile_list)
		time.sleep(1)
		printer(pile_list)
		
		if list_of_previous_new_pile_lists[0] == list_of_previous_new_pile_lists[1]:	
			return "GAME OVER, YOU WENT OUT!\n"
		elif cycle_estimation(list_of_all_pile_lists,pile_list):
			return "CONGRATULATIONS, YOU WON BY CYCLE!\n"
		elif stage == 24:
			return "CONGRATULATIONS, YOU WON!\n"

def combination_size_estimation(pile_combinations_list):
	"""
	1. A list of all combinations is inputted.
	2. The function determines whether the pile list is going to be selected by the user or randomly selected depending on the size of the combinations.
	3. The returned object is the pile list. 
	"""
	if len(pile_combinations_list) <= 25:
		return choice_and_test(printing_combination_choices(pile_combinations_list))
	elif len(pile_combinations_list) > 25:
		print("\nYou have",len(pile_combinations_list),"possible combinations. \nRandomly selected:\n ")
		return random.choice(pile_combinations_list)

def remove_duplicates(list_of_all_combinations):
	"""
	1. A list of all sorted combinations is inputted. 
	2. This function removes all the duplicates in the list. 
	3. The sorted list is then returned.
	"""
	pile_combinations_list = []
	for combination in list_of_all_combinations:
		if combination not in pile_combinations_list:
			pile_combinations_list.append(combination)
	return pile_combinations_list

def counting_combinations(number_of_cards , v_num, k, com_list, list_of_all_combinations, add):
	"""
	1. There are 6 parameters coming in to this recursion function.
	2. All combinations for the card number given by the player is calculated here. That heppens through a recursion algorithm and the combinations are saved in a list. 
	3. The returned object is the list of all possible combinations.
	"""
	if add:
		com_list.append(add)
	if v_num == 0 or (k+1) == number_of_cards:
		if (k+1) == number_of_cards and v_num > 0:
			com_list.append(v_num)
			k += 1
		list_of_all_combinations.append(delete_zeros(com_list))
		return list_of_all_combinations
	for x in range(1,v_num+1):																			# Recursion happens (a.k.a Tree)
		counting_combinations(number_of_cards ,v_num-x, k+1, com_list[:], list_of_all_combinations,x)  	# v_num,com_list och x har samma värde tills funktionen ger en fördelning där summan blir lika med number_of_cards 
	return list_of_all_combinations

def choice_and_test(pile_combinations_list):	
	"""
	1. List of pile combinations is inputted.
	2. This function is used only if the combinations are few enough to be able to choose the desired one. The choice is then converted to integer and checks if the choice is an available choice.
	3. The function returns the chosen pile list only if every requiement is fulfilled.
	"""
	while True:
		try:
			choice= int(input("Please choose one of the combination piles above: "))
			if 0< choice <= len(pile_combinations_list):
				pile_list= pile_combinations_list[choice-1]
				return pile_list
			else:
				print("Incorrect!")
		except:
			print("Incorrect!")	

def printing_combination_choices(pile_combinations_list): 
	"""
	1. List of pile combinations is inputted.
	2. Prints the combinations in a numbered order so the player can make a choice.
	3. Returns the same pile combinations list.
	"""
	choice_number=1
	while choice_number <= len(pile_combinations_list):
		for combination in pile_combinations_list:
			print(choice_number,":", end="   ")
			for batch in combination:
				print(batch,end=" ")
			print("\n")
			choice_number+= 1
	return pile_combinations_list

def integer_input_test(number_of_cards):
	"""
	1. The input number of cards is coming in to this function.
	2. Estimates whther the the input number is an integer and appropriate.
	3. Return only a True or False signal.
	"""
	try:
		number_of_cards=int(number_of_cards)
		if 1< number_of_cards <53:
			return True 
	except:
		return False

def menu():
	#Initiation of the game programme. The user has to input the number of cards he wants to play with and then the programme is initiated.
	print(
	"""
				WELCOME TO BULGARIAN SOLITAIRE GAME


The Rules of Bulgarian Solitaire:

Bulgarian solitaire is a mathematical game in which you have to choose a number of cards and devide them in piles. 
One card is taken from each card and a new pile is made of the taken cards. The process continues until you are stuck in a loop.
1. If the loop is has the same numbers of piles repeatedly, then you have lost the game.
2. If the loop cycles around with different numbers after each round, then you have won.
3. And if the game doesn't stuck in a loop for 25 rounds, then you've also won.

Enjoy!


""")
	while True:
		number_of_cards= input("How many cards do you want to play with (between 2 and 52): ")
		if integer_input_test(number_of_cards):
			number_of_cards=int(number_of_cards)
			print(game_run(combination_size_estimation(remove_duplicates(counting_combinations(number_of_cards ,number_of_cards, 0, [], [], None)))))
			time.sleep(10)
			os.system('cls' if os.name=='nt' else 'clear')
		else:
			os.system('cls' if os.name=='nt' else 'clear')
			print("Your choice has to be in numbers, between 2 and 52. Please try again!")
	return

menu()


