from iPyQT import *

# Window = BasicWindow(250, 250, "Title")
# Window.create()


Ben = CustomWindow(300, 350, "Title of Application")
Ben.create()
text2 = Ben.addText("Text 2", 50, "None")
Ben.move(50, 5, text2, "Text")
Ben.printInfo()
Ben.init()