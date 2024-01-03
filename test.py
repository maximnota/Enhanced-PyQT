from iPyQT import *

# Window = BasicWindow(50, 50, "Title")
# Window.create()

def smthRandom():
    print("Hello")
def jerry():
    print("Jerry has been clicked upon")
def bob():
    print("Bob Has been clicked upon")

CustomWindow = CustomWindow(300, 350, "Title of Application")
CustomWindow.create()
CustomWindow.createRadioGroupBox("Test")
jerry = CustomWindow.addChoiceButton("Jerry", jerry)
bob = CustomWindow.addChoiceButton("Bob", bob)
text1 = CustomWindow.addText("Text", 50, "Right-top")
text2 = CustomWindow.addText("Text 2", 25, "Left-bottom")
button1 = CustomWindow.addButton("Button", smthRandom)
CustomWindow.printInfo()
CustomWindow.init()

