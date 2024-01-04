from iPyQT import *

# Window = BasicWindow(250, 250, "Title")
# Window.create()

def smthRandom():
    print("Hello")



def jerry():
    print("Jerry has been clicked upon")
    textFieldValue = Ben.getTextFieldValue(TextField)
    print(textFieldValue)
    

def bob():
    print("Bob Has been clicked upon")

Ben = CustomWindow(300, 350, "Title of Application")
Ben.create()
Ben.createRadioGroupBox("Test")
jerry = Ben.addChoiceButton("Jerry", jerry)
bob = Ben.addChoiceButton("Bob", bob)
text1 = Ben.addText("Text", 50, "Right-top")
text2 = Ben.addText("Text 2", 25, "Left-bottom")
button1 = Ben.addButton("Button", smthRandom)
TextField = Ben.addTextField(30, 40, "Center")
Ben.printInfo()
Ben.init()

