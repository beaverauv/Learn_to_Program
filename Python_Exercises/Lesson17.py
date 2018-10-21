#That was one ugly line of code! Let's make a function that can add any amount of numbers that we want
#If we define a parameter with an = in it, then if that parameter is not defined it will by default be what you set it to
#That sounds complicated but just watch


def additionV3(number1, number2, number3=0, number4=0, number5=0, number6=0):
        return number1 + number2 + number3 + number4 + number5 + number6


print(additionV3(1,2,3,4,5,5))
