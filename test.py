from iPyQT import *

# Window = BasicWindow(250, 250, "Title")
# Window.create()
Ben = CustomWindow(300, 350, "Title of Application")
Ben.create()
text2 = Ben.addText("Text 2", 25, "Center")
Ben.changeTextColor(text2, "red")
Ben.printInfo()
Ben.init()

