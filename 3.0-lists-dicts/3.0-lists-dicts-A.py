myList = [] # houdt een order aan
myDict = {} # houdt een kvp aan (key-value pair)

fruits = []

myFruit = "Cactus fruit"

fruits.append('Apple')
fruits.append('Banana')
fruits.append(myFruit)

print(fruits)
print(fruits[1])

print(fruits.index(myFruit))

print("---------------")

myPerson = {'name': 'John', 'age': 20, 'email': 'john@doe.com'}
print(myPerson)
personsAge = myPerson['age']

# myPerson['age'] = 30
print(personsAge)