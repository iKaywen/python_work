print("If you could visit one place in the world, where would you go?")
responses={}
while True:
	name = input("What is your name: ")
	response = input("Where would you go for vacation? ")
	#把健和值存在字典里。
	responses[name] = response
	repeat = input("Do you wish to proceed with more survey questions? ")
	if repeat == 'no':
		break
for name, response in responses.items():
	print(name+" would like to go to "+response+" for vacation!")