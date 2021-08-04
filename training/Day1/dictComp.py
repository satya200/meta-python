
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d1 :{d1}")

d2 = {item for item in d1}
print(f"d2 :{d2}")

print("-" * 40)
d3 = {item for item in d1.keys()}
print(f"d3 :{d3}")

print("-" * 40)
d4 = {item for item in d1.values()}
print(d4)

print("-" * 40)
d5 = {item for item in d1.items()}
print(d5)

print("-" * 40)
d6 = {k: v for k, v in d1.items()}
print(d6)

d7 = {v: k*2 for k, v in d1.items()}
print(d7)

squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(squares)

print("-" * 40)
players = {
    'sachin': [300, 250, 350, 420, 385],
    'rahul': [402, 325, 350, 280, 390],
    'sehwag': [440, 375, 480, 315, 360],
    'yuvraj':[190, 220, 308, 345, 310],
    'vvs':[225, 175, 190, 205, 150]
}

print(players)

print("-" * 40)
plyrScores = {k: sum(v) for k, v in players.items()}
print(plyrScores)

print("-" * 40)
plyrScores = {k: (lambda scores: sum(scores) / len(scores))(v)
              for k, v in players.items()}
print(plyrScores)

print("-" * 40)
plyrScores = [runs for runs in players.values()]
print(plyrScores)

print("-" * 40)
plyrScores = [x for runs in players.values() for x in runs]
print(plyrScores)

print("-" * 40)
plyrScores = [x for runs in players.values() for x in runs if x > 200]
print(plyrScores)

print("-" * 40)
plyrScores = {name: [scr for scr in scores if scr > 200]
              for name, scores in players.items()}
print(plyrScores)
