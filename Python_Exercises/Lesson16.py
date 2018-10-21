#Now that you have a basic understanding of functions, lets complicate things a bit
#You can put a function in the parameter of another function. Here check it out:

#Instead of saving the result of the function off in another variable, this can be much more compacted

def additionV2(number1, number2):
        return number1 + number2 #changed print to return

whatis2and5 = additionV2(2,5)

adding8 = additionV2(whatis2and5, 8)

print(adding8)




print(additionV2(additionV2(2,5), 8))

