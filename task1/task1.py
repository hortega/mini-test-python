import collections

"""
Count how many Apples, Pears, Lemons, Oranges, Pineapples, Tomatoes, 
Mangoes and Bananas are in the list.

Expected output:
Apple: 2,
Pear: 3
Lemon: 2,
Orange: 1,
Pineapple: 2,
Tomato: 1,
Mango: 1
Banana: 0
"""

task1 = [
    "apple",
    "pear",
    "lemon",
    "orange",
    "pineapple",
    "tomato",
    "lettuce",
    "mango",
    "apple",
    "pineapple",
    "lemon",
    "pear",
    "pear",
]
fruits = ['apple', 'pear', 'lemon', 'orange', 'pineapple', 'tomato', 'mango', 'banana']

counter = collections.Counter(task1)

for fruit in fruits:
    print(f'{fruit.capitalize()}: {counter[fruit]}')


