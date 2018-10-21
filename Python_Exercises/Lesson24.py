#Moving onto one of the most powerful parts of python, lets start with an issue
#Lets say I have a dog, and it has these variables

name = "Pupperico"
color = "White"
breed = "Husky"
age = 6.0
isAGoodBoi = True

#Now what if I got another dog? Then these would have to make some more variables

dog1name = "Pupperico"
dog1color = "White"
dog1breed = "Husky"
dog1age = 6.0
dog1isAGoodBoi = True

dog2name = "Fluffer"
dog2color = "Golden"
dog2breed = "Retreiver"
dog2age = 2.5
god2isAGoodBoi = True


#Now this works, but it looks ugly and if we want to adopt 100 dogs it becomes a pain
#This is where classes come into play. Basically, you make a template for our dog and it will keep track of the specifics

class Dog:
	def __init__(self, name, color, breed, age, isAGoodBoi):
		self.name = name
		self.color = color
		self.breed = breed
		self.age = age
		self.isAGoodBoi = isAGoodBoi

dog1 = Dog("Pupperico", "White", "Husky", 6.0, True)
dog2 = Dog("Fluffer", "Golden", "Retreiver", 2.5, True)


#Isn't that a lot easier????
