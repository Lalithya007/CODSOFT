import string
import random
length = int(input("Enterlength: ") )

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4.exit''')

characterList = ""
c=0

while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		characterList += string.ascii_letters
	elif(choice == 2):
		characterList += string.digits
	elif(choice == 3):
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	randomchar = random.choice(characterList)
	password.append(randomchar)
print("The random password is " + "".join(password))
