word = input("Enter any word:")
letters_in_word = len(word)
number = int(input("Enter a number:"))

product = letters_in_word * number
output = ""
if product % 3 == 0 or product % 5 == 0:
	if product % 3 == 0:
		output += "foo"
	if product % 5 == 0:
		output += "bar"
	print output
else:
	print word * product