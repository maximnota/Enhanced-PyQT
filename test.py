from iPyQT import *
win = CustomWindow(300, 350, "Window")
win.create()
Text = win.addText("Text", 25, "None")
win.move(200, 50, Text, "Text")
win.init()