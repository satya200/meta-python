"""
comprehension is iterating through a list using lambda syntax
"""
# lambdas

def add(x, y):
    return x + y

a = add
res = a(100, 200)
print(res)

l = lambda x, y: x + y
res = l(10, 20)
print(res)

print("-" * 40)
fruits = [
    ('apple', 250),
    ('grapes', 140),
    ('orange', 95),
    ('banana', 45),
    ('watermelon', 70),
    ('strawberry', 380),
    ('gauva', 60)
]

print(fruits)
prices = ['fruits' for fruit in fruits ]
print(prices)

print("-" * 40)
prices = [fruit for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[0] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(prices)

print("-" * 40)
prices = [(fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(prices)

print("-" * 40)
expnFruits = [(fruit[0], fruit[1], fruit[1] * 0.9) for fruit in fruits if fruit[1] >= 100]
print(expnFruits)

squares = [x ** 2 for x in range(1, 11)]
print(squares)
