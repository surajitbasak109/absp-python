import os
for folderName, subfolders, filenames in os.walk('/home/rex/absp'):
	print('Folder name: ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER FOR ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('INSIDE OF ' + folderName + ': ' + filename)
