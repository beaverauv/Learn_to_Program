#So why do we use functions? Cause it can do a lot of code in just line and can make things easier
#Last thing before the next project: the return command. Lets take our old function addition

#addition(4, 8)
#this just printed the result, but what if we wanted to use the result later in the code?
#This is where we use return. Return makes the output of the function equal to whatever you put in the return line. Here, let me show you


def additionV2(number1, number2):
	return number1 + number2 #changed print to return

#Now lets use this function

whatis2and5 = additionV2(2,5)

adding8 = additionV2(whatis2and5, 8)

print(adding8)



Using the additionV2 function, add the numbers 4, 7, 12, and 19 and print the sum
