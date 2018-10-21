#Heres something trippy: what if I put an array inside an array? Well this is something done more commonly than you'd think

insideArray1 = [1,2,3]
insideArray2 = [4,5,6]
insideArray3 = [7,8,9]

outsideArray = [insideArray1, insideArray2, insideArray3]

#You can even access the elements in the inside arrays with more brackets

print(outsideArray[0][0])

#Now make your own print statement that prints out the number 7 using the arrays
