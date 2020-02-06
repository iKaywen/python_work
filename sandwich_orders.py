#7-9#7-10
sandwich_orders = ['turkey', 'pastrami', 'veggie', 'pastrami', 'roast beef', 'pastrami']
print("we are out of pastrami")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders) 
finished_sandwiches =[]
while sandwich_orders:
	processed_sandwich = sandwich_orders.pop()
	print("I made your "+processed_sandwich.title()+" sandwich!")
	finished_sandwiches.append(processed_sandwich)
for finished_sandwich in finished_sandwiches:
	print("Finished sandwiches are: "+finished_sandwich+" sandwich!")
