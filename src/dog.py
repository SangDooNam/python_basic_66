from animal import Animal

class Dog(Animal):
    
    #TODO create a constructor for Dog, with 4 legs and 2 eyes!
    def __init__(self, number_of_legs=4, number_of_eyes=2):
        super().__init__(number_of_legs, number_of_eyes)

    #TODO override the breathe() method!
    def breathe(self):
        super().breathe()
        print("Dogs love to breathe with their mouths open.")
    #TODO override the walk() method!
    def walk(self):
        super().walk()
        print("Dogs love to run.")
