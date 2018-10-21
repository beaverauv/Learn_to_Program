#Changing the subject for a second, what if I wanted to print out all the numbers between 1 and 100?
#I could do this...

print("1")
print("2")
print("3")
#and so on...
#but thats a lot of work, why do that when we can put it into a loop?


#like a function, this declares what this is
#|	#this variable will be set to whatever changes in our for loop
#|       |	the range() function makes an array of numbers between 1 and 100 (it starts at the first number and ends at the last number -1 since arrays are 0 indexed) 
#|       |       |    first number
#|       |       |    |   second number
#|	 |	 |    |	 |
for number in range(1, 101):
	print(number)
