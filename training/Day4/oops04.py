
class Player:

    # double underscore = dunder init
    def __init__(self, name, age):
        self.name = name        # attributes or instance variables
        self.age = age
        print("Player Initialized.....")

    def get_details(self):      # methods
        print(f"name={self.name} and age={self.age}")

ply1 = Player("Sachin", 38)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 36)
ply2.get_details()
