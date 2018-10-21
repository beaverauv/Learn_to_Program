#Now what if we want these classes to do stuff? Well classes are also able to be given their own functions

class Dog:
        def __init__(self, name, color, breed, age, isAGoodBoi):
                self.name = name
                self.color = color
                self.breed = breed
                self.age = age
                self.isAGoodBoi = isAGoodBoi
	
	def isPlaying(self):
		print(self.name + " is playing")
	
	def testIfGoodBoi(self):
		if self.isAGoodBoi == True:
			print("Of course " + self.name + " is a good boi!")
		else:
			print("ERROR 404: GOOD BOI NOT FOUND")

dog1 = Dog("Pupperico", "White", "Husky", 6.0, True)
dog2 = Dog("Fluffer", "Golden", "Retreiver", 2.5, True)

#Now try to call isPlaying() on dog1 and testIfGoodBoi on dog2
#Hint: It's similar to how you get properties of a class
