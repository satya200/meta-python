
class Player:

    def __init__(self, name, age):
        print("Init")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"name={self.name} and age={self.age}")

    @classmethod
    def CreatePlayer(cls, name, age):       # Factory
        print('Factory')
        return cls(f"Mr.{name}", age)

sachin = Player("Tendulkar", 38)
sachin.get_details()

print("-" * 40)
ply1 = Player.CreatePlayer("Virat", 32)
ply1.get_details()

