import random
randomnum = random.randint(1, 50)
print("The random number is ", randomnum)
num = int(input("Please enter a number from 1 to 50 "))
#print("The number entered is ", num)
while num != randomnum:
    if num > randomnum:
        num = int(input("The number entered is bigger, Please enter smaller number "))
    elif (num < randomnum):
        num = int(input("The number entered is smaller, Please enter bigger number "))
print("Thank you, you guessed it right")