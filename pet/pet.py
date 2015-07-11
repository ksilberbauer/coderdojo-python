import random

def get_random_photo():
    return random.choice(['(=^o.o^=)__', '<:3 )~~~~', '<`)))><', '(^0M0^)'])

class Pet:
    """A pet"""

    def __init__(self, name, photo):
        self.name = name
        self.photo = photo
        self.is_hungry = True
        self.age = 0
        self.weight = random.randint(1, 10)
        self.favorite_foods = []
    
    def selfie(self):
        return self.photo
    
    def feed(self, food):
        """Returns True if pet is not hungry (after feeding, if necessary)"""
        if not self.is_hungry:
            print "I'm not hungry"
            return True
        elif len(self.favorite_foods) > 0 and food not in self.favorite_foods:
            print "I don't like that food. Do you have one of these?"
            for favorite in self.favorite_foods:
                print favorite
            return False
        elif len(self.favorite_foods) is 0:
            self.favorite_foods += input("What are my favorite foods again?").split(",")
        else:
            self.is_hungry = False
            print "Mmmm, delicious!"
            return True
    
    def __str__(self):
        return """
        name: %s
        photo: %s
        age: %s
        weight: %s
        hungry?: %s
        favorite foods: %s 
        """ % (
            self.name, 
            self.photo, 
            str(self.age) + ' years old', 
            str(self.weight) + 'lbs', 
            'Yes' if self.is_hungry else 'No', 
            str.join(',', self.favorite_foods)
        )
