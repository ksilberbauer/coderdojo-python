my_pet = {
    'age': 5,
    'weight': 9,
    'hungry': True,
    'photo': '(=^o.o^=)__',
    'favorite foods': ['milk', 'fish', 'lasagna', 'cat food']
}

my_pet['name'] = input("What is your pet's name?")

# This function works for any dictionary with 'hungry' and 'favorite foods' properties
def feed(pet):
    favorite_foods = pet['favorite foods']
    if pet['hungry']:
        print "I'm hungry!"
        while input("What do you want to feed your pet?") not in favorite_foods:
            print "I don't like that food. I want one of these:"
            for food in favorite_foods:
                print food
        pet['hungry'] = False
        print "Mmm, yummy, thanks!"
    else:
        print "I just ate"

print 'Hello, my name is ' + my_pet['name']
print my_pet['photo']

feed(my_pet)