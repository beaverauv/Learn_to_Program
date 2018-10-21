#Heres something cool about functions. Ever hear of recursion? Well your about to
#Recursion means that inside the function it calls itself, which is really trippy
#This means it could keep going forever and ever (eventually crashing your program) so its important that you include an if statement in it so it knows when to stop
#Heres a cool function that does the factorial operation recursively

def factorial(number):
	if number == 1:
		return 1
	else:
		return number * factorial(number-1)

print(factorial(7))


#Note: there are very few times you will use recursion since it takes quite a bit of processing power, and using this in a for loop would be very slow for your computer
