#!/usr/bin/env python3

d = dict()
print(d)
print(type(d))

print("-" * 40)
d1 = dict({'a': 'apple', 'b': 'ball', 'c': 'cat'})
print(d1)
print(type(d1))

print("-" * 40)
d2 = dict([('name', 'sachin'), ('age', 46), ('runs', 23500), ('matches', 435)])
print(d2)
print(type(d2))

print("-" * 40)
d3 = dict(name='rahul', age=35, dept='Fin', des='MGR', sal=85000)
print(d3)
print(type(d3))

print("-" * 40)
player = {'name': 'sachin', 'runs': 16500, 'odis': 350}
print(f"player :{player}")
print(player['name'])
print(player.get('odis', "key is invalid, please enter a valid key"))

for k, v in player.items():
    print(k + " => " + str(v))

print("-" * 40)
player['age'] = 48
print(player)

player['runs'] = 18000
print(player)

del player['odis']
print(player)
