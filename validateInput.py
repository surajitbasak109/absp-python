while True:
	print("What is your age?")
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')
	
while True:
	print("Select a new password (letter and numbers only)")
	pw = input()
	if pw.isalnum():
		break
	print('Passwords can only have numbers and letters')
