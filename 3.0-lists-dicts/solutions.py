"""Simple solutions for the beginner exercises in exercises.md

Run this file to see the outputs for each exercise.
"""

def ex1():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print('ex1 ->', fruits)


def ex2():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print('ex2 ->')
    for i in range(len(fruits)):
        print(f"{i}: {fruits[i]}")


def ex3():
    colors = []
    colors.append('red')
    colors.append('green')
    colors.append('blue')
    colors.remove('green')
    print('ex3 ->', colors)


def ex4():
    nums = [0, 1, 2, 3, 4, 5]
    print('ex4 ->', nums[1:5])


def ex5():
    nums = [2, 4, 6]
    avg = sum(nums) / len(nums)
    print('ex5 ->', avg)


def ex6_and_7():
    person = {'name': 'Ana', 'age': 30}
    person['city'] = 'Amsterdam'
    person['age'] = 31
    print('ex6 ->', person)
    print('ex7 ->')
    for k, v in person.items():
        print(f"{k} -> {v}")


def ex8():
    words = ['apple', 'banana', 'apple', 'cherry']
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    print('ex8 ->', counts)


def ex9():
    data = {'students': [{'name': 'Ana'}, {'name': 'Ben'}]}
    print('ex9 ->', data['students'][1]['name'])


def ex10():
    person = {'name': 'Ana', 'age': 31}
    print('ex10 ->', person.get('email', 'no-email'))


def run_all():
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6_and_7()
    ex8()
    ex9()
    ex10()


if __name__ == '__main__':
    run_all()
