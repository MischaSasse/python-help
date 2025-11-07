# maak door gebruik van een loop het volgende zien in je terminal:
# *
# **
# ***
# ****
# *****

star = "*"
space=" "
for i in range(1,6):
    print(f"{space*(6-i)}{star*i}{star*(i-1)}")




food = []
grains = ['corn', 'wheat', 'amaranth', 'quinoa', 'rice']
fruits = ['banana','pear','apple','apricot', 'mango']
vegetables = ['carrot', 'cucumber', 'onion', 'garlic', 'eggplant']

food.append(grains)
food.append(fruits)
food.append(vegetables)

# gebruik een loop om alle stukken fruit te laten zien
for fruit in food[1]:
    print(fruit)

# voor de mensen met al programmeer ervaring, probeer de volgende twee uitkomsten te krijgen
#      *
#     **
#    ***
#   ****
#  *****
# en
#      *
#     ***
#    *****
#   *******
#  *********



# Exercise 1 — for-range: print even numbers from 0 up to (but not including) 'limit'
# Change 'limit' to see more or fewer numbers.
limit = 10  

print('\nExercise 1: for-range — even numbers <', limit)
for i in range(limit):
    if i % 2 == 0:
        print(i)


# Exercise 2 — foreach (for item in list): filter and print items starting with a letter
# Change 'items' and 'start_letter' to practice.
items = [] 

print(f"\nExercise 2: foreach - items starting with ''")
for item in items:
    # add logic to only show items starting with a specific letter     
    print()


# Exercise 3 — while loop: countdown (inclusive) from 'start' to 0
# Change 'start' to try different countdown lengths. Be careful not to set a negative
# number if you want to see the countdown.
start = 5  # try 3, 0

print(f"\nExercise 3: while — countdown from {start}")
cnt = start
while cnt >= 0:
    print(cnt)
    cnt = -5


# Exercise 4 — nested loops (multiplication table 1..n)
# Change 'n' to produce a larger or smaller table.
n = 4  # try 3 or 5

print(f"\nExercise 4: nested loops — multiplication table 1..{n}")
for a in range(1, n + 1):
    # print a single row for multiplier 'a'
    row = ''
    for b in range(1, n + 1):
        row += f"{a*b}\t"
    print(row)


if __name__ == '__main__':
    print('\nKlaar — pas de variabelen boven elke oefening aan en run opnieuw.')
