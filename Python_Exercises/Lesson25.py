#Now how do we use the data for these two dogs? It's super simple and it's just like this...

class Dog:
        def __init__(self, name, color, breed, age, isAGoodBoi):
                self.name = name
                self.color = color
                self.breed = breed
                self.age = age
                self.isAGoodBoi = isAGoodBoi

dog1 = Dog("Pupperico", "White", "Husky", 6.0, True)
dog2 = Dog("Fluffer", "Golden", "Retreiver", 2.5, True)

print("My first dog's name is " + dog1.name)
print("My first dog's name is " + dog2.name)


#Now print out the ages and breeds of the two dogs on your own
