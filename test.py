from iPyQT import *

# Window = BasicWindow(50, 50, "Title")
# Window.create()

CustomWindow = CustomWindow(300, 350, "Something here", "Banana", 25, "Right-center", "Test")
CustomWindow.printInfo()
CustomWindow.create()
CustomWindow.addChoiceButton("Jerry")

CustomWindow.init()
