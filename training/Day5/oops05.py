
class Player:

    # double underscore = dunder init
    def __init__(self, name, age):
        self.name = name        # attributes or instance variables
        self.age = age
        print("Player Initialized.....")

    # setter method used to add new attributes
    def set_iplteam(self, team):
        self.team = team

    # getter methods used to display the attribute values
    def get_details(self):      # methods
        print(f"name={self.name} and age={self.age}")

    def get_team(self):
        print(f"team is {self.team}")

ply1 = Player("Sachin", 38)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 36)
ply2.set_iplteam("RR")
ply2.get_details()
ply2.get_team()

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 40)
ply2.runs = 85      # Expando
print(ply2.__dict__)
print(ply1.__dict__)
