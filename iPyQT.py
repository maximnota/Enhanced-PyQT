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
    def __init__(self, height, width, title, text, textSize, Alignment, RadioGroupBoxName, RadioGroupBoxPosition):
        self.height = height
        self.width = width
        self.title = title
        self.text = text
        self.Alignment = Alignment
        self.textSize = textSize
        self.RadioGroupBoxName = RadioGroupBoxName
        self.RadioGroupBoxPosition = RadioGroupBoxPosition
    
    def printInfo(self):
        print("Title: ", self.title)
        print("Height: ", self.height)
        print("Width: ", self.width)
        print("Text: ", self.text)

    def create(self):
        app = QApplication([])

        global v_line
        v_line = QVBoxLayout()

        global CustomWin
        CustomWin = QWidget()
        CustomWin.setWindowTitle(self.title)
        CustomWin.resize(self.height, self.width)

        global Text
        Text = QLabel()
        Text.setText(self.text)
        font = Text.font()
        font.setPointSize(self.textSize)
        Text.setFont(font) 

        if self.RadioGroupBoxName != "N/A" and self.RadioGroupBoxPosition == 0:
            Box = QGroupBox(self.RadioGroupBoxName)
            v_line.addWidget(Box)

        if self.Alignment == "Center":
            print("Center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignCenter)

        elif self.Alignment == "None":
            print("No Alignment")
            v_line.addWidget(Text)

        elif self.Alignment == "Right-top":
            print("Right-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignTop)

        elif self.Alignment == "Right-bottom":
            print("Right-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignBottom)

        elif self.Alignment == "Right-center":
            print("Right-center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignHCenter)

        elif self.Alignment == "Center-top":
            print("Center-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignTop)

        elif self.Alignment == "Center-bottom":
            print("Center-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignBottom)

        elif self.Alignment == "Left-top":
            print("Left-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignTop)

        elif self.Alignment == "Left-center":
            print("Left-center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignHCenter)

        elif self.Alignment == "Left-bottom":
            print("Left-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignBottom)

        if self.RadioGroupBoxName != "N/A" and self.RadioGroupBoxPosition == 1:
            Box = QGroupBox(self.RadioGroupBoxName)
            v_line.addWidget(Box)

        CustomWin.setLayout(v_line)
        
        CustomWin.show()

        app.exec_()
        app.setActiveWindow()
    
