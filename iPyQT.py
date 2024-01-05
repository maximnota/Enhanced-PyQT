from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

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
    
class CustomWindow():
    def __init__(self, height, width, title):
        self.height = height
        self.width = width
        self.title = title
        self.ChoiceButtons = []
        self.Buttons = []
        self.TextFields = []
        self.Texts = []
        self.RadioGroupBoxes = []
        self.BoxLayouts = []

    def printInfo(self):
        print("Title: ", self.title)
        print("Height: ", self.height)
        print("Width: ", self.width)



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


    def addRadioGroupBox(self, RadioGroupBoxName):
        global Box
        Box = QGroupBox(RadioGroupBoxName)
        self.RadioGroupBoxes.append(Box)
        v_line.addWidget(Box)
        i = 0
        for box in self.RadioGroupBoxes:
            if box == Box:
                RadioGroupBoxID = i
                break
            i += 1
        return RadioGroupBoxID

    def addChoiceButton(self, buttonName, function):
        Button = QRadioButton(buttonName)
        self.ChoiceButtons.append(Button)
        h_line.addWidget(Button)
        Box.setLayout(h_line)
        Button.clicked.connect(function) 
        i = 0
        for cbutton in self.ChoiceButtons:
            if cbutton == Button:
                ChoiceButtonID = i
                break
            i += 1
        return ChoiceButtonID

    
    def addButton(self, buttonName, function):
        Button = QPushButton(buttonName)
        self.Buttons.append(Button)
        v_line.addWidget(Button)
        Button.clicked.connect(function)
        i = 0
        for button in self.Buttons:
            if button == Button:
                ButtonID = i
                break
            i += 1

        return ButtonID

    
    
    def addText(self, text, textSize, Alignment):
        Text = QLabel()
        Text.setText(text)
        font = Text.font()
        font.setPointSize(textSize)
        Text.setFont(font) 
        self.Texts.append(Text)
        i = 0


        for txt in self.Texts:
            if txt == Text:
                TextID = i
                break
            i += 1

        match Alignment:
            case "Center":
                print("Center Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignCenter)
            case "None":
                print("No Alignment")
                v_line.addWidget(Text)                
            case "Right-top":
                print("Right-top Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignTop)
            case "Right-bottom":
                print("Right-bottom Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignBottom)
            case "Right-center":
                print("Right-center Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignRight | Qt.AlignHCenter)
            case "Center-top":
                print("Center-top Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignTop)
            case "Center-bottom":
                print("Center-bottom Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignHCenter | Qt.AlignBottom)
            case "Left-top":
                print("Left-top Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignTop)
            case "Left-center":
                print("Left-center Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignHCenter)
            case "Left-bottom":
                print("Left-bottom Alignment")
                v_line.addWidget(Text, alignment=Qt.AlignLeft | Qt.AlignBottom)
        return TextID

    def addTextField(self, height, width, Alignment):
        global textBox
        textBox = QLineEdit()
        textBox.resize(height, width)
        self.TextFields.append(textBox)
        a = 0

        for field in self.TextFields:
            if field == textBox:
                textBoxID = a
                break
            a += 1
        
        match Alignment:
            case "Center":
                print("Center Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignCenter)
            case "None":
                print("No Alignment")
                v_line.addWidget(textBox)                
            case "Right-top":
                print("Right-top Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignTop)
            case "Right-bottom":
                print("Right-bottom Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignBottom)
            case "Right-center":
                print("Right-center Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignRight | Qt.AlignHCenter)
            case "Center-top":
                print("Center-top Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignHCenter | Qt.AlignTop)
            case "Center-bottom":
                print("Center-bottom Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignHCenter | Qt.AlignBottom)
            case "Left-top":
                print("Left-top Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignTop)
            case "Left-center":
                print("Left-center Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignHCenter)
            case "Left-bottom":
                print("Left-bottom Alignment")
                v_line.addWidget(textBox, alignment=Qt.AlignLeft | Qt.AlignBottom)

        return textBoxID

    def getTextFieldValue(self, ID):
        return self.TextFields[ID].text()
    


    def HideAll(self):  
        print("Hide All")
        for Text in self.Texts:
            Text.hide()
        for Button in self.Buttons:
            Button.hide()
        for cButton in self.ChoiceButtons:
            cButton.hide()
        for radioGroupBox in self.RadioGroupBoxes:
            radioGroupBox.hide()
        for textField in self.TextFields:
            textField.hide()
        
    
    def ShowAll(self):
        print("Show all")
        for Text in self.Texts:
            Text.show()
        for Button in self.Buttons:
            Button.show()
        for cButton in self.ChoiceButtons:
            cButton.show()
        for radioGroupBox in self.RadioGroupBoxes:
            radioGroupBox.show()
        for textField in self.TextFields:
            textField.show()       
    
    def HideObject(self, objectType, objectID):
        match objectType:
            case "Text":
                self.Texts[objectID].hide()
            case "Button":
                self.Buttons[objectID].hide()
            case "ChoiceButton":
                self.ChoiceButtons[objectID].hide()
            case "textField":
                self.TextFields[objectID].hide()
            case "RadioGroupBox":
                self.RadioGroupBoxes[objectID].hide()

    def ShowObject(self, objectType, objectID):
        match objectType:
            case "Text":
                self.Texts[objectID].show()
            case "Button":
                self.Buttons[objectID].show()
            case "ChoiceButton":
                self.ChoiceButtons[objectID].show()
            case "textField":
                self.TextFields[objectID].show()
            case "RadioGroupBox":
                self.RadioGroupBoxes[objectID].show()
    

    def changeText(self, ID, Text):
        self.Texts[ID].setText(Text)


    def changeFont(self, objectType, ID, customFont, Size):
        match objectType:
            case "Text":
                self.Texts[ID].setFont(customFont, Size)
            case "Button":
                self.Buttons[ID].setFont(customFont, Size)
            case "ChoiceButton":
                self.ChoiceButtons[ID].setFont(customFont, Size)
            case "TextField":
                self.TextFields[ID].setFont(customFont, Size)
            
    def changeTextColor(self, ID, color):
        a = "color: "
        b = a + color
        self.Texts[ID].setStyleSheet(b)
    
    def changeWindowColor(self, color):
        a = "background-color: "
        b = a + color
        CustomWin.setStyleSheet(b)

    #To Fix
    def move(self, new_x, new_y, objectID, objectType):
        match objectType:
            case "Text":
                self.Texts[objectID].move(new_x, new_y)
            case "Button":
                self.Buttons[objectID].move(new_x, new_y)
            case "ChoiceButton":
                self.ChoiceButtons[objectID].move(new_x, new_y)
            case "textField":
                self.TextFields[objectID].move(new_x, new_y)
            case "RadioGroupBox":
                self.RadioGroupBoxes[objectID].move(new_x, new_y)       

    def init(self):
        app.exec_()