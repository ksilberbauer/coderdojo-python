from <CodeSkulptor user for Pet module> import Pet, get_random_photo

name = input("What is your pet's name? ")
my_pet = Pet(name, get_random_photo())

print my_pet.selfie()

favorite_foods = input("What are you pet's favorite foods? (separate foods with commas)").split(",")
my_pet.favorite_foods += favorite_foods

while my_pet.is_hungry:
    food = input("What do you want to feed your pet?")
    my_pet.feed(food)

print my_pet