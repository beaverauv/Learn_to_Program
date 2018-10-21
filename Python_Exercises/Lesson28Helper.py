class Dog:
        def __init__(self, name, color, breed, age, isAGoodBoi):
                self.name = name
                self.color = color
                self.breed = breed
                self.age = age
                self.isAGoodBoi = isAGoodBoi

        def isPlaying(self):
                print(self.name + " is playing")
	
	def whatAnimal(self):
		return "Dog"

class Cat:
	 def __init__(self, name, color, breed, age, isAGoodBoi):
                self.name = name
                self.color = color
                self.breed = breed
                self.age = age
                self.isAGoodGirl = isAGoodBoi

         def whatAnimal(self):
                return "Dog"

