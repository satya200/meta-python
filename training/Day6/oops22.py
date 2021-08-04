
import oops21
# print(dir(oops21))

def withDraw():
    print("You can withdraw Rs. 2000 per day")

# monkey patching
hdfc = oops21.HDFC()
hdfc.withDraw = withDraw
hdfc.withDraw()
