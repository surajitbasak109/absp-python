mypets = ['zophie', 'Duke', 'Tom', 'Fat-Tail']
print('Enter a pet name:')
name = input()
if name not in mypets:
    print('I do not have pet named ', name)
else:
    print(name, 'is my pet.')
