pet = {
    'age': 5,
    'weight': 9,
    'hungry': True,
    'photo': '(=^o.o^=)__',
    'favorite foods': ['milk', 'fish', 'lasagna', 'cat food']
}

pet['name'] = input("What is your pet's name?")

print 'Hello, my name is ' + pet['name']
print pet['photo']

if pet['hungry']:
    print "I'm hungry!"
    print "My favorite foods are:"
    for food in pet['favorite foods']:
        print food
    print "Can I have one of those?"
else:
    print "I just ate"