# <- this is a comment, it allows you to explain your code

# variables store values
# these are 'string' variables; they store text
string_1 = "This is a string. It's just text"
string_2 = 'You can use single or double quotes for strings'

first_name = "George"
last_name = "Washington"

# if you want to combine strings (called 'string concatenation'), you the '+' sign
full_name = first_name + " " + last_name 

# the print statement writes output
print full_name # prints "George Washington" (without the quotes)

# you can also treat numbers as strings...
number_as_string_1 = "2"
number_as_string_2 = str(2) # convert a number to a string

# ... but they stop working like numbers (so math doesn't work)
numbers = "2" + str(2) # what is the value of 'numbers' variable? hint: it's not 4

print numbers # prints "22", because the '+' sign smashes two strings together