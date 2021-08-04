
class Player:       # pascal casing

    def __init__(self):  # constructor
        print("Player initialized....")

    # self will store the name of the object which called getRuns method
    def getRuns(self):
        print("runs scored....")


sachin = Player()      # call the constructor
sehwag = Player()
rahul = Player()

sachin.getRuns()
rahul.getRuns()