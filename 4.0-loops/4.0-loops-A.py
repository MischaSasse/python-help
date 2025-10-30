# wanneer we het over loops hebben, hebben we het over iteraties. je gaat een x aantal keer door de code heen.

for i in range(0,5):
    print(i)
# i start bij de eerste waarde in range(), in dit geval 0.
# hierna runt het de code, daarna komt er 1 bij i 
# is de nieuwe waarde van i nu nog steeds kleiner dan de tweede waarde in range, dan runt de code weer.

fruits = ["apple", "pear", "dragonfruit", "banana", "watermelon"]

for i in range(len(fruits)):
    print(fruits[i])

print("------------")

for fruit in fruits:
    print(fruit)

print("------------")

x = 5
while x <= 10:
    print(x)
    x+=1
# zolang while (condition = true): run code
# zorg er wel voor dat als je een variabel oid hebt, 
# dat deze verandert in de while-loop zodat je geen infinite loop hebt