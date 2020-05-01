'''t = (1, 2, 3)
print(t[0])
t = (123456789, "Suman", True)
print(t[2])
creditcard1 = ("1234", "Suman")
creditcard2 = ("5678", "Palisetty")
creditcards = [creditcard1, creditcard2]
print(creditcards)'''
person1 = ("suman", 25, "pizza")
person2 = ("palisetty", 37, "panipuri")
person = [ person1, person2]
'''(name, age, fav) = person
print(name)
print(age)
print(fav)'''
for name, age, fav in person:
    print(name)
    print(age)
    print(fav)
    print("")