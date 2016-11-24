while True:
	print('Who are you?')
	name = input()
	if(name != 'Surajit'):
		continue
	print('Hello, ',name, ' What is your password? (It is a fish)')
	password = input()
	if(password == 'swordfish'):
		break
print('Access granted')
