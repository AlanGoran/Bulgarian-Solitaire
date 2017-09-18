import time
def input_function():
	pile_list= []
	print("Welcome to Bulgarian Solitaire Game")
	number_of_piles= int(input("How many piles of cards do you want: "))
	for x in range(1,number_of_piles+1):
		number_of_cards= int(input("Number of cards in this deck: "))
		pile_list.append(number_of_cards)
	return pile_list

def round_play(pile_list):
	for batch in range(len(pile_list)):
		pile_list[batch]= pile_list[batch]-1
	pile_list.append(len(pile_list))
	return pile_list

def delete_zeros(pile_list):
	pile_list.sort(reverse=True)
	return [batch for batch in pile_list if batch != 0]

def printer(pile_list):
	for batch in pile_list:
		print(batch,end=" ")
	print("\n")

def loser_winner_estimation(pile_list,new_pile_list):
	new_pile_list= delete_zeros(round_play(pile_list))
	if pile_list==new_pile_list:
		return True
	elif pile_list!=new_pile_list:
		return False

def cycle_estimation(list_of_all_pile_lists,pile_list):
	for previous_pile_list in list_of_all_pile_lists:
		if previous_pile_list == pile_list:
			return True

def main():
	pile_list= input_function()
	printer(pile_list)
	list_of_all_pile_lists=[]
	for stage in range(25):
		list_of_all_pile_lists.append(delete_zeros(pile_list))
		print(list_of_all_pile_lists)
		list_of_previous_new_pile_lists=[delete_zeros(pile_list)]
		pile_list= delete_zeros(round_play(pile_list))
		list_of_previous_new_pile_lists.append(pile_list)
		time.sleep(1)
		printer(pile_list)
		if list_of_previous_new_pile_lists[0] == list_of_previous_new_pile_lists[1]:
			print("You are out")
			break
		elif cycle_estimation(list_of_all_pile_lists,pile_list):
			print("cycle")
			break 
		elif stage == 24:
			print("Congrats, you won")
	return 

main()
