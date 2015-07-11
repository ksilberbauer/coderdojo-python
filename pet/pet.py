class Pet:
    """A pet"""
    def __init__(self, name, age, weight, photo, favorite_foods):
        self.name = name
        self.age = age
        self.weight = weight
        self.photo = photo
        self.favorite_foods = favorite_foods
        self.is_hungry = True
    def selfie(self):
        print """
            %s
        """ % self.photo
    def feed(self):
        if self.is_hungry:
            print "I'm hungry!"
            while input("What do you want to feed your pet?") not in self.favorite_foods:
                print "I don't like that food. I want one of these:"
                for food in self.favorite_foods:
                    print food
            self.is_hungry = False
            print "Mmm, yummy, thanks!"
        else:
            print "I just ate"
    def __str__(self):
        return """
        Hi! My name is %s.
        I'm %i years old, and I weigh %i lbs.
        """ % (self.name, self.weight, self.age)

name = input("What is your pet's name?")
age = int(input("How old is your pet?"))
weight = int(input("How much does your pet weigh?"))
photo = input("What should your pet look like?")
favorite_foods = input("Does your pet have any favorite foods? (separate foods by commas)").split(",")

my_pet = Pet(name, age, weight, photo, favorite_foods)
another_pet = Pet("Fred", 2, 10, "<`)))><", ["water", "shrimp"])



print my_pet
my_pet.selfie()
my_pet.feed()
print "\n\n"
print another_pet
