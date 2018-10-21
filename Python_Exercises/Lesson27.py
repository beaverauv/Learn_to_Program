#For this next lesson, make an instance of class Dog called evilDog and give it the name Nick and set isAGoodBoi to False
#Next, make a new function for class Dog called whatIsItDoing() and have it print "NAME is doing evil things"
#Finally, call whatIsItDoing() and testIfGoodBoi() on class instance evilDog 
#I'm tired so don't blame me for the weird question

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

