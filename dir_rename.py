'''
Allows the user to rename all the files in a directory sequentially.
Adapted from a geeksforgeeks article.
'''

import os

def main():
	#Get current working directory (CWD)
	path = os.getcwd()
	folder = ''
	
	while folder != '!exit':
		print('Input a directory to rename the files in it. The directory must be a subdirectory of the CWD.')
		print('CWD = ' + path)
		print('Type !exit to exit.')
		folder = input('>')
		
		if folder == '!exit':
			break
		
		if folder == '':
			print('Please input a directory name.')
		else:
			print('\nInput a new base name for each file in this directory.\nFor example, \'foo\' will yield foo1.jpg, foo2.png, foo3.exe, etc.')
			name = input('>')
			
			if name == '':
				print('Please input a file name.')
			elif name == '!exit':
				break
			else:			
				#Concatenate the path and the folder
				path = os.path.join(path, folder)
				
				try:
					#For each file in this directory...
					for count, filename in enumerate(os.listdir(path)):
						#Get the extension
						splt = filename.split('.')
						if len(splt) == 1:
							ext = ''
						else:
							ext = splt[1]
						
						#Concatenate source file path
						src = os.path.join(path, filename)
						
						#Assemble destination filename and concatenate its path
						dst = name + str(count) + '.' + ext
						dst = os.path.join(path, dst)

						#print(src)
						#print(dst)
						#Rename
						os.rename(src, dst)
				except FileNotFoundError:
					print('\tError: Directory does not exist.\n')
	
main()
