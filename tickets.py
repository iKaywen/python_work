print("please enter your age")
while True:
	prompt = input("Please enter your age: ")
	if prompt != 'quit':
		if int(prompt) < 3:
			print("Free admission!")
		elif int(prompt) <= 12:
			print("10 bucks.")
		else:
			print("15 bucks.")
	else:
		print("you are all set")
		break

