
class Player:
    team = "India"

    def __init__(self, name, age):
        self.name = name        # attributes or instance variables
        self.age = age
        print("Player Initialized.....")

    def get_details(self):      # methods
        print(f"name={self.name} and age={self.age}")

sachin = Player("Tendulkar", 38)
rahul = Player("Dravid", 37)

sachin.get_details()
rahul.get_details()
print(Player.team)
print(sachin.team)
print(rahul.team)

print("-" * 40)
Player.team = "RCB"
print(Player.team)
print(sachin.team)
print(rahul.team)

print("-" * 40)
sachin.team = "MI"
print(sachin.team)
print(Player.team)
print(rahul.team)

print("-" * 40)
print(sachin.__dict__)
print(rahul.__dict__)
print(Player.__dict__)
