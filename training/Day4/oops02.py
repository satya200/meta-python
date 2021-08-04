
class Player:

    def getRuns(self):
        print("Method :", self.__class__)
        print("runs scored....")

sachin = Player()       # call default constructor
sachin.getRuns()

print(type(sachin))
print(sachin.__class__)

print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
