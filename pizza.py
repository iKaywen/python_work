#prompt = input("Please select the toppings on your pizza: ")
#prompt+= input("Enter 'quit' when you are finished. ")
print("Please select the toppings on your pizza, and quit if you are finished.")
#active = True
#while active:
while True:
	prompt = input()
	#prompt+= input("Enter 'quit' when you are finished. ")
	if prompt == 'quit':
		#active = False
		print("you are all set!")
		break
	else:
		print("We have added: "+prompt.title()+" on your pizza!")	


