
#Imports for all the things that this library needs.
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

#class declaration to create basic windows for testing purposes
class BasicWindow():
    def __init__(self, height, width, title):
        #Creates variables that are needed to be inputted when creating this class. The variables will then be able to be used throughout this class
        self.height = height
        self.width = width
        self.title = title

    def printInfo(self):
        # A simple function that takes the parameters inside of the class and uses the print function to display them.
        print("Height: ", self.height)
        print("Width: ", self.width)
        print("Title: ", self.title)
    
    def create(self):
        # Creates a basic window
        app = QApplication([])
        # Creates the application class.
    
        global win
        win = QWidget()

        #Created the window widget which is accessible throughout other functions if needed.
        win.setWindowTitle(self.title)
        #Setting the window title to what the class parameters set it to.
        win.resize(self.height, self.width)
        #Setting the size to what the class parameters want it to be.
        win.show()
        #Makes the window widget have the ability to be visible
        app.exec_()
        app.setActiveWindow()
        # Executes the application and shows the window
    
#A more customisable way of creating windows.
class CustomWindow():
    def __init__(self, height, width, title):
        self.height = height
        self.width = width
        self.title = title
        # Adds the class parameters needed to create the window.
        self.ChoiceButtons = []
        self.Buttons = []
        self.TextFields = []
        self.Texts = []
        self.RadioGroupBoxes = []
        self.BoxLayouts = []
        self.Images = []
        # Lists that are needed for later functions so that they will persist throughout the runtime of the class.

    def printInfo(self):
        #Prints out the basic info of the window
        print("Title: ", self.title)
        print("Height: ", self.height)
        print("Width: ", self.width)


    #Creates the window
    def create(self):
        global app
        app = QApplication([])

        # Creates a global variable called app that will be used later.

        global h_line
        h_line = QHBoxLayout()
        # Global variable h_line is used for layouts later.
        global v_line
        v_line = QVBoxLayout()
        # Global variable v_line is used for layouts later.

        global CustomWin
        CustomWin = QWidget()
        CustomWin.setWindowTitle(self.title)
        CustomWin.resize(self.height, self.width)

        # Custom window is a window widget that takes the window parameters given when creating the class initially

        CustomWin.setLayout(v_line)
        # Sets a layout style called v_line that was declared before.
        
        CustomWin.show()
        # Gives the ability to CustomWin to be displayed
        app.setActiveWindow(CustomWin)
        # Sets the CustomWin as the window that will be displayed when starting the app.


    def addRadioGroupBox(self, RadioGroupBoxName):
        # A function that adds
        global Box
        Box = QGroupBox(RadioGroupBoxName)
        # Declaring the box variable as global so that other functions can use it. The box is used to create a visible box that also has a title with it.
        self.RadioGroupBoxes.append(Box)
        # Adds the box to the radio group boxes list that I declared in the __init__ for persistence.
        v_line.addWidget(Box)

        # Adds the box to a layout line so that it has a proper place to be placed.
        
        i = 0
        for box in self.RadioGroupBoxes:
            # Indexes through the boxes while increasing the variable i + 1 every iteration.
            if box == Box:
                # Checks if the box element in the list is equal to the one from this function.
                RadioGroupBoxID = i
                # Sets the id variable of the box element to i.
                break
                # Stops the loop
            i += 1
        return RadioGroupBoxID
        # Returns the variable RadioGroupBoxID 

    def addChoiceButton(self, buttonName, function):
        #Declares a function in the class called addChoiceButton with its own parameters.
        Button = QRadioButton(buttonName)
        # Creates a radio button with the text given in from the function parameters.
        
        self.ChoiceButtons.append(Button)
        # Adds the button into the choicebuttons list for persistence.
        
        h_line.addWidget(Button)
        # Adds the Button to the horizontal layout line.
        Box.setLayout(h_line)
        # Sets the layout for the global variable Box which is defined in the previous function.
        Button.clicked.connect(function)
        # Adds a function to be executed when the button was clicked on.
        i = 0
        for cbutton in self.ChoiceButtons:
            # Itereates through the choice buttons and every iteration increases i + 1.
            if cbutton == Button:
                #Checks if choice button is equal to the button currently in this function.
                ChoiceButtonID = i
                # Declares a variable choice button id to the value of i.
                break
                # Stops the loop
            i += 1
        return ChoiceButtonID
        #Returns the choice button id.

    
    def addButton(self, buttonName, function):
        # Declares a function for creating normal buttons.
        Button = QPushButton(buttonName)
        # Declares variable button.
        self.Buttons.append(Button)
        # Adds button to the list of buttons inside of the class for persistence throughout the runtime of the class.
        v_line.addWidget(Button)
        # Adds the button to the v_line layout line for alignment.
        Button.clicked.connect(function)
        i = 0
        for button in self.Buttons:
            # Itereates through the normal buttons and every iteration increases i + 1.
            if button == Button:
                #Checks if normal button is equal to the button currently in this function.
                ButtonID = i
                # Declares a variable button id to the value of i.
                break
                # Stops the loop
            i += 1

        return ButtonID
        #Returns the choice button id.

    
    
    def addText(self, text, textSize, Alignment):
        # Declares a function for creating text labels.
        Text = QLabel()
        # Declares variable text.
        Text.setText(text)
        # Sets the text inside of the text label to the text provided in the function parameter.
        font = Text.font()
        # Declares a font variable that will hold font data.
        font.setPointSize(textSize)
        # Sets the font size of the font variable to the one provided in the function parameter.
        Text.setFont(font) 
        # Sets the font of the text to the one provided in the function parameter.

        self.Texts.append(Text)
        # Adds the text variable to the text list initially declared in the beggining of the class in the __init__.
        i = 0


        for txt in self.Texts:
            # Iterates through the list of texts and each iteration increases i by 1.
            if txt == Text:
                # Checks if the text currently indexed in the iteration is equal to the one created in the function
                TextID = i
                # Sets the id of the text to the variable i.
                break
                # Breaks the loop
            i += 1
    

        match Alignment:
        #Creates a match statement to see what alignment the user selected. The selected alignment must be one of the pre implemented ones. Then when the sleected alignment is matched it will be set to that alignment.
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
        # Returns the Text ID variable.

    def addTextField(self, height, width, Alignment):
        # Creates a function called add text field which is used for creating text fields.
        global textBox
        textBox = QLineEdit()
        # Creates a global variable for the text box.
        textBox.resize(height, width)
        # Sets the size of the text box to the one provided in the function parameter.
        self.TextFields.append(textBox)
        # Appends the text to the text list provided in the initialisation of the class.
        a = 0

        for field in self.TextFields:
            # Iterates through all text fields and increases a by 1.
            if field == textBox:
                # Checks if the indexed text field is equal to the one creaeted in the function.
                textBoxID = a
                # Declares the text box id variable with the value of the variable a.
                break
                # Breaks the loop.
            a += 1
        #Creates a match statement to see what alignment the user selected. The selected alignment must be one of the pre implemented ones. Then when the sleected alignment is matched it will be set to that alignment.
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
        #Returns the text box id.

    def getTextFieldValue(self, ID):
        # Declares a function for getting the text field value inside of the text.
        return self.TextFields[ID].text()
        # Returns the text field value by indexing it using the id returned in the function that created it.
    


    def HideAll(self):  
        # A function for hiding all elements.
        print("Hide All")
        for Text in self.Texts:
            # Goes through all text elements.
            Text.hide()
            # Hides the indexed text.
        for Button in self.Buttons:
            # Goes through all button elements.
            Button.hide()
            # Hides the indexed button.
        for cButton in self.ChoiceButtons:
            # Goes through all choice button elements.
            cButton.hide()
            # Hides the indexed button.
        for radioGroupBox in self.RadioGroupBoxes:
            # Goes through all radio group box elements.
            radioGroupBox.hide()
            # Hides the radio group box element.
        for textField in self.TextFields:
            # Goes through all radio group box elements.
            textField.hide()
            # Hides the text field element.
        for image in self.Images:
            # Goes through all image elements.
            image.hide()
            # Hides the image element.
        
    
    def ShowAll(self):
        # A function for showing all the elements which does the same thing as the hide all function but instead of the hide function it uses the show function to make the elements visible.
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
        for image in self.Images:
            image.show()
    
    def HideObject(self, objectType, objectID):
        # Declares a function for hiding a specific object.
        match objectType:
            # Matches the object type so that it can be corrrectly indexed in its relevant list and then the .hide() fuction is used on it.
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
            case "Image":
                self.Images[objectID].hide()

    def ShowObject(self, objectType, objectID):
        # The same function as the HideObject function but it shows the object instead by using the .show() function.
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
            case "Image":
                self.Images[objectID].show()
    

    def changeText(self, ID, Text):
        # A function for changing the text value of a text.
        self.Texts[ID].setText(Text)
        # Changes the value of the text by indexing the text from the texts list and setting it to the text provided in the function parameters.


    def changeFont(self, objectType, ID, customFont, Size):
        font = QFont(customFont, Size)
        match objectType:
            case "Text":
                print("Text")
                self.Texts[ID].setFont(font)
            case "Button":
                self.Buttons[ID].setFont(font)
            case "ChoiceButton":
                self.ChoiceButtons[ID].setFont(font)
            case "TextField":
                self.TextFields[ID].setFont(font)
            
    def changeColor(self, objectType, ID, color):
        a = "color: "
        b = a + color
        match objectType:
            case "Text":
                self.Texts[ID].setStyleSheet(b)
            case "Button":
                self.Buttons[ID].setStyleSheet(b)
            case "ChoiceButton":
                self.ChoiceButtons[ID].setStyleSheet(b)
            case "TextField":
                self.TextFields[ID].setStyleSheet(b)

    def addTextBorder(self, objectID, thickness, style, color):
        border_style = f"{thickness}px {style} {color}"
        self.Texts[objectID].setStyleSheet(f"border: {border_style};")


    def addImage(self, image_path, width, height):
        image = QPixmap(image_path)
        Image = QLabel()
        Image.setPixmap(image)
        Image.resize(width, height)
        v_line.addWidget(Image)
        self.Images.append(Image)
        i = 0
        for picture in self.Images:
            if picture == Image:
                ImageID = i
                break
            i += 1
        return ImageID

    def changeWindowOpacity(self, newOpacity):
        CustomWin.setWindowOpacity(newOpacity)
    
    def changeBackgroundColor(self, objectType, ID, color):
        a = "background-color: "
        b = a + color
        match objectType:
            case "Text":
                self.Texts[ID].setStyleSheet(b)
            case "TextField":
                self.TextFields[ID].setStyleSheet(b)

    def resizeObject(self, objectType, objectID, new_x, new_y):
        match objectType:
            case "Text":
                self.Texts[objectID].resize(new_x, new_y)
            case "Button":
                self.Buttons[objectID].resize(new_x, new_y)
            case "ChoiceButton":
                self.ChoiceButtons[objectID].resize(new_x, new_y)
            case "TextField":
                self.TextFields[objectID].resize(new_x, new_y)
            case "Image":
                self.Images[objectID].resize(new_x, new_y)


    def changeWindowColor(self, color):
        a = "background-color: "
        b = a + color
        CustomWin.setStyleSheet(b)

    def changeImage(self, objectID, image_path, width, height):
        image = QPixmap(image_path)
        self.Images[objectID].setPixmap(image)
        self.Images[objectID].resize(width, height)

    def changeWindowTitle(self, newTitle):
        CustomWin.setWindowTitle(newTitle)

    def changeWindowIcon(self, icon_path):
        icon = QIcon(icon_path)
        CustomWin.setWindowIcon(icon)

    
    def move(self, new_x, new_y, objectID, objectType):
        print("Checking type")
        match objectType:
            case "Text":
                label = self.Texts[objectID]
                widget_layout = v_line
                widget_layout.removeWidget(label)    
                widget_layout.addWidget(label, alignment=Qt.AlignLeft | Qt.AlignTop)
                widget_layout.setContentsMargins(new_x, new_y, 0, 0)  # Set new position      
                widget_layout.update()
            case "Button":
                button = self.Buttons[objectID]
                widget_layout = v_line
                widget_layout.removeWidget(button)    
                widget_layout.addWidget(button, alignment=Qt.AlignLeft | Qt.AlignTop)
                widget_layout.setContentsMargins(new_x, new_y, 0, 0)  # Set new position      
                widget_layout.update()
            case "TextField":
                textField = self.TextFields[objectID]
                widget_layout = v_line
                widget_layout.removeWidget(textField)    
                widget_layout.addWidget(textField, alignment=Qt.AlignLeft | Qt.AlignTop)
                widget_layout.setContentsMargins(new_x, new_y, 0, 0)  # Set new position      
                widget_layout.update()
            case "Image":
                self.Images[objectID].move(new_x, new_y)

    def changeButtonText(self, objectID, text):
        self.Buttons[objectID].setText(text)

    def init(self):
        app.exec_()
