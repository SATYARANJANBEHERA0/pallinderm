def Pallinderm(string):
	if (string == string[::-1]):
		print('The string is pallinderm')
	else:
		print('The string is not pallinderm')
s = input('Enter a string:')
string = s.lower()
Pallinderm(string)