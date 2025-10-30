myList = [] # houdt een order aan
myDict = {} # houdt een kvp aan (key-value pair)
# beide zijn mutable (ze kunnen veranderen) tov oa een string

fruits = []

myFruit = "Cactus fruit"

fruits.append('Apple')
fruits.append('Banana')
fruits.append(myFruit)

fruits.insert(1, "lemon")

# je kan ook .extend gebruiken om dingen van een list2 toe te voegen aan list1, maar kan ook voor tuples, sets, ect
myTuple = ("orange", "kiwi")
# een tuple wordt gebruikt om meerdere items in 1 variabel te bewaren (also tuples kan je niet aanpassen)

print(myTuple[0])
fruits.extend(myTuple)

print(fruits)
print(fruits[1])

print(fruits.index(myFruit))

print("---------------")

myPerson = {'name': 'John', 'age': 20, 'email': 'john@doe.com'}
print(myPerson)
personsAge = myPerson['age']
print(personsAge)

myPerson.update({'job': 'chef'})
myPerson['country'] = 'The Netherlands'
myPerson = {**myPerson, 'city': 'Almere'}
myPerson = dict(myPerson, happyWithMajor= 'No')
# 4 manieren om iets toe te voegen aan een dict

print(myPerson)