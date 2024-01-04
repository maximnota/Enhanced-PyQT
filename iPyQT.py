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
    def __init__(self, height, width, title):
        self.height = height
        self.width = width
        self.title = title
        self.ChoiceButtons = []
        self.Buttons = []
        self.Box = None
        self.Text = None
        self.TextFields = []
    
    def printInfo(self):
        print("Title: ", self.title)
        print("Height: ", self.height)
        print("Width: ", self.width)
        print("Text: ", self.Text)



    def create(self):
        global app
        app = QApplication([])

        global h_line
        h_line = QHBoxLayout()
        global v_line
        v_line = QVBoxLayout()

        global CustomWin
        CustomWin = QWidget()
        CustomWin.setWindowTitle(self.title)
        CustomWin.resize(self.height, self.width)

        CustomWin.setLayout(v_line)
        
        CustomWin.show()
        app.setActiveWindow(CustomWin)


    def createRadioGroupBox(self, RadioGroupBoxName):
        self.Box = QGroupBox(RadioGroupBoxName)
        v_line.addWidget(self.Box)

    def addChoiceButton(self, buttonName, function):
        Button = QRadioButton(buttonName)
        self.ChoiceButtons.append(Button)
        h_line.addWidget(Button)
        self.Box.setLayout(h_line)
        Button.clicked.connect(function) 

    
    def addButton(self, buttonName, function):
        Button = QPushButton(buttonName)
        self.Buttons.append(Button)
        v_line.addWidget(Button)
        Button.clicked.connect(function)

    
    
    def addText(self, text, textSize, Alignment):
        Text = QLabel()
        Text.setText(text)
        font = Text.font()
        font.setPointSize(textSize)
        Text.setFont(font) 
    
        if Alignment == "Center":
            print("Center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignCenter)

        elif Alignment == "None":
            print("No Alignment")
            v_line.addWidget(Text)

        elif Alignment == "Right-top":
            print("Right-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignTop)

        elif Alignment == "Right-bottom":
            print("Right-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignBottom)

        elif Alignment == "Right-center":
            print("Right-center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignHCenter)

        elif Alignment == "Center-top":
            print("Center-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignTop)

        elif Alignment == "Center-bottom":
            print("Center-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignBottom)

        elif Alignment == "Left-top":
            print("Left-top Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignTop)

        elif Alignment == "Left-center":
            print("Left-center Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignHCenter)

        elif Alignment == "Left-bottom":
            print("Left-bottom Alignment")
            v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignBottom)

    def addTextField(self, height, width, Alignment):
        global textBox
        textBox = QLineEdit()
        textBox.resize(height, width)
        textBoxID = len(self.TextFields)
        self.TextFields.append(textBox)
        
        if Alignment == "Center":
            print("Center Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignCenter)

        elif Alignment == "None":
            print("No Alignment")
            v_line.addWidget(Text)

        elif Alignment == "Right-top":
            print("Right-top Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignTop)

        elif Alignment == "Right-bottom":
            print("Right-bottom Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignBottom)

        elif Alignment == "Right-center":
            print("Right-center Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignHCenter)

        elif Alignment == "Center-top":
            print("Center-top Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignHCenter | Qt.AlignTop)

        elif Alignment == "Center-bottom":
            print("Center-bottom Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignHCenter | Qt.AlignBottom)

        elif Alignment == "Left-top":
            print("Left-top Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignTop)

        elif Alignment == "Left-center":
            print("Left-center Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignHCenter)

        elif Alignment == "Left-bottom":
            print("Left-bottom Alignment")
            v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignBottom)

        return textBoxID

    def getTextFieldValue(self, ID):
        return self.TextFields[ID].text()
    
    def Hide(self):
        CustomWin.hide()

    def init(self):
        app.exec_()
