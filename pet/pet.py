name = input("What is your pet's name?")
age = 5
weight = 9
hungry = True
photo = '(=^o.o^=)__'

favorite_foods = ['milk', 'fish', 'lasagna', 'cat food']

print 'Hello, my name is ' + name
print photo

if hungry:
    print "I'm hungry!"
    print "My favorite foods are:"
    for food in favorite_foods:
        print food
    print "Can I have one of those?"
else:
    print "I just ate"