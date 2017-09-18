import os
import time
import random

def round_play(pile_list):
	for batch in range(len(pile_list)):
		pile_list[batch]= pile_list[batch]-1
	pile_list.append(len(pile_list))
	return pile_list

def delete_zeros(pile_list):
	pile_list.sort(reverse=True)
	return [batch for batch in pile_list if batch != 0]

def printer(pile_list): 						#????????????????????????????????????????????????
	for batch in pile_list:
		print(batch,end=" ")
	print("\n")

def cycle_estimation(list_of_all_pile_lists,pile_list):
	for previous_pile_list in list_of_all_pile_lists:
		if previous_pile_list == pile_list:
			return True

def combination_size_estimation(all_pile_combinations_list):
	if len(all_pile_combinations_list) <= 30:
		return True
	elif len(all_pile_combinations_list) > 30:
		return False

def remove_duplicates(list_of_all_combinations):
	all_pile_combinations_list = []
	for i in list_of_all_combinations:
		if i not in all_pile_combinations_list:
			all_pile_combinations_list.append(i)
	return all_pile_combinations_list

def game_run(pile_list):
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
			return "You are out \n"	
		elif cycle_estimation(list_of_all_pile_lists,pile_list):
			return "Cycle, you won \n"
		elif stage == 24:
			return "Congrats, you won \n"

def count_combs(number_of_cards ,left, i, comb, list_of_all_combinations, add):
	if add:
		comb.append(add)
	if left == 0 or (i+1) == number_of_cards:
		if (i+1) == number_of_cards and left > 0:
			comb.append(left)
			i += 1
		list_of_all_combinations.append(delete_zeros(comb))
		return list_of_all_combinations
	for x in range(1,left+1):															# Recursion Tree happens
		count_combs(number_of_cards ,left-x, i+1, comb[:], list_of_all_combinations,x)  # left,comb och x har samma värde tills funktionen ger en fördelning där summan blir lika med number_of_cards 
	return list_of_all_combinations

def choice_and_test(all_pile_combinations_list):	# BORTA	
	while True:
		try:
			choice= int(input("Please choose one of the combination piles above: "))
			if 0< choice <= len(all_pile_combinations_list):
				return all_pile_combinations_list[choice-1]
		except:
			print("Incorrect!")	

def printing_combination_choices(all_pile_combinations_list): 					#??????????????????????????????????????????
	choice_number=1
	while choice_number <= len(all_pile_combinations_list):
		for combination in all_pile_combinations_list:
			print(choice_number,":", end="   ")
			for batch in combination:
				print(batch,end=" ")
			print("\n")
			choice_number+= 1
	return all_pile_combinations_list

def input_test(number_of_cards): 					# BORTA
	try:
		number_of_cards=int(number_of_cards)
		if 1< number_of_cards <53:
			return number_of_cards #game_run(combination_size_estimation(remove_duplicates(count_combs(number_of_cards ,number_of_cards, 0, [], [], None))))
		else:
			return "Your answer has to be in numbers, between 2 and 52. Please try again!"
	except:
		return "Your answer has to be in numbers, between 2 and 52. Please try again!"

def integer_input_test(number_of_cards):
		try:
			number_of_cards=int(number_of_cards)
			if 1< number_of_cards <53:
				return True 
		except:
			return False

def main():
	print("\nWELCOME TO BULGARIAN SOLITAIRE GAME\nBLA BLA BLA BLA\n")
	while True:
		number_of_cards= input("How many cards do you want to play with (between 2 and 52): ")
		if integer_input_test(number_of_cards):
			number_of_cards=int(number_of_cards)
			all_pile_combinations_list= remove_duplicates(count_combs(number_of_cards ,number_of_cards, 0, [], [], None))
			if combination_size_estimation(all_pile_combinations_list):
				printing_combination_choices(all_pile_combinations_list)
				while True:
					try:
						choice= int(input("Please choose one of the combination piles above: "))
						if 0< choice <= len(all_pile_combinations_list):
							pile_list= all_pile_combinations_list[choice-1]
							break
						else:
							print("Incorrect!")
					except:
						print("Incorrect!")	
			else:
				print("\nYOU HAVE",len(all_pile_combinations_list),"POSSIBLE COMBINATIONS. \nRANDOMLY SELECTED:\n ")
				pile_list= random.choice(all_pile_combinations_list)
			os.system('cls' if os.name=='nt' else 'clear')
			print(game_run(pile_list))
			time.sleep(5)
			os.system('cls' if os.name=='nt' else 'clear')
		else:
			os.system('cls' if os.name=='nt' else 'clear')
			print("Your choice has to be in numbers, between 2 and 52. Please try again!")
	return

main()