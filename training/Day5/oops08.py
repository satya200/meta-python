
# Magic Methods
class Player:
    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f"name={self.name} and age={self.age}"

ply1 = Player("Sachin", 48)
print(ply1)
print(str(ply1))