## Beginner exercises — Lists and Dictionaries

These exercises are very small, self-contained tasks meant for absolute beginners.
Try them in order. Each exercise includes a short hint and an example of expected output.

1) Create and print a list
   - Task: Make a list named `fruits` with 5 fruit names and print it.
   - Hint: `fruits = ['apple', 'banana', ...]`
   - Expected: `['apple', 'banana', 'cherry', 'date', 'elderberry']` (order may vary)

2) Loop with range and indexes
   - Task: Using `range(len(fruits))`, print each index and its fruit.
   - Hint: `for i in range(len(fruits)):` then use `fruits[i]`.
   - Expected lines:
     - `0: apple`
     - `1: banana`

3) Add and remove elements
   - Task: Start with an empty list `colors = []`. Append three colors, then remove one by value.
   - Hint: use `append()` and `remove()`.
   - Expected: list with two colors.

4) Slicing
   - Task: Given `nums = [0,1,2,3,4,5]`, print the slice containing the middle numbers (1..4).
   - Hint: use `nums[1:5]`.
   - Expected: `[1, 2, 3, 4]`

5) Sum and length
   - Task: Given a list of integers, compute and print the average (sum / len).
   - Hint: Use `sum()` and `len()`.
   - Expected: For `[2,4,6]` average is `4.0`.

6) Create and modify a dictionary
   - Task: Create `person = {'name': 'Ana', 'age': 30}`. Add a key `city`, then change `age` to 31.
   - Hint: `person['city'] = '...'`, `person['age'] = 31`
   - Expected: `{'name': 'Ana', 'age': 31, 'city': '...'}` (order may vary)

7) Iterate over dict keys and values
   - Task: Print all keys and values in `person` using `.items()`.
   - Hint: `for k, v in person.items():`
   - Expected lines like `name -> Ana` and `age -> 31`.

8) Word/count frequency (small)
   - Task: Given the list `words = ['apple', 'banana', 'apple', 'cherry']`, build a dict `counts` that maps each word to how often it appears.
   - Hint: Initialize empty dict and increment: `counts[w] = counts.get(w, 0) + 1`
   - Expected: `{'apple': 2, 'banana': 1, 'cherry': 1}` (order may vary)

9) Nested structures (access)
   - Task: Given `data = {'students': [{'name':'Ana'}, {'name':'Ben'}]}`, print the name of the second student.
   - Hint: `data['students'][1]['name']`
   - Expected: `Ben`

10) Small extra challenge — safe lookup
   - Task: Use `dict.get()` to safely read `person['email']` but return `'no-email'` if missing.
   - Hint: `person.get('email', 'no-email')`
   - Expected: `no-email` if `email` not present.

---

Answers are provided in `solutions.py`. Try solving on your own first, then run the solutions to compare.
