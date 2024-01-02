from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class BasicWindow():
    def __init__(self, height, width, title):
        self.height = height
        self.width = width
        self.title = title

    def printInfo(self):
        print("Height: ", self.height)
        print("Width: ", self.width)
        print("Title: ", self.title)
    
    def create(self):
        app = QApplication([])

        global win
        win = QWidget()
        win.setWindowTitle(self.title)
        win.resize(self.height, self.width)
        win.show()

        app.exec_()
        app.setActiveWindow()

    def hide(self):
        win.hide()

class CustomWindow():
    def __init__(self, height, width, title, text, textHeight, textWidth, Alignment):
        self.height = height
        self.width = width
        self.title = title
        self.text = text
        self.textHeight = textHeight
        self.textWidth = textWidth
        self.Alignment = Alignment
    
    def printInfo(self):
        print("Title: ", self.title)
        print("Height: ", self.height)
        print("Width: ", self.width)
        print("Text: ", self.text)

    def create(self):
        app = QApplication([])

        v_line = QVBoxLayout()
        v1_line = QVBoxLayout()
        v2_line = QVBoxLayout()
        v3_line = QVBoxLayout()

        h_line = QHBoxLayout2()
        h1_line = QHBoxLayout()
        h2_line QHBoxLayout()

        global CustomWin
        CustomWin = QWidget()
        CustomWin.setWindowTitle(self.title)
        CustomWin.resize(self.height, self.width)

        global Text
        Text = QLabel()
        Text.setText(self.text)
        Text.resize(self.textHeight, self.textWidth)

        if self.Alignment == "Center":
            v_line.addWidget(Text, alignment=Qt.AlignCenter)
        if self.Alignment == "None":
            v_line.addWidget(Text)
        if self.Alignment == "Right-top":


        CustomWin.setLayout(v_line)
        
        CustomWin.show()

        app.exec_()
        app.setActiveWindow()