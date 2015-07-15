# the input function allows you to prompt the user for input
# (note: some versions of Python call this function raw_input)

name = input("What is your name?") # in CodeSkulptor, opens a popup window with an input box
age = input("How old are you?") # important note: the input is always considered a 'string'

print "My name is " + name
print "I am " + age + " years old"
print "In five years I will be " + str(int(age) + 5) + " years old" # this line may look confusing:
# remember, in Python you can only do math if both variables are 'int', so we first convert 'age' from string to int
# then we add 5 to it (also an int), then convert the sum back to string, so that we can concatenate it with the other text

# 'if' statements allow you to choose between multiple paths of code
if int(age) > 16: # this is the 'if condition'; it is a statement that evaluates to True or False
    print "I can drive!"
else: # if the 'if condition' is False, the else statement will run intead
    print "I'm too young to drive"

# you can have multiple alternatives as well:
if int(age) < 13:
    print "I'm not a teenager yet"
elif int(age) < 18: # notice that the 'elif' statement is a combination between the words 'else' and 'if'
    print "I'm a teenager"
elif int(age) < 65: # it allows you to check another 'if condition', but only if the ones before it were False
    print "I'm an adult"
else:
    print "I'm a senior citizen"