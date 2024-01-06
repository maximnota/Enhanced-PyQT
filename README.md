# Enhanced PyQT

This application is built using PyQt5 to create a customizable window with various widgets and functionalities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Introduction

The **CustomWindow** application provides a customizable window using PyQt5, allowing users to create and manage various widgets within the window. The application provides functionalities to add buttons, text fields, choice buttons, and more, with options to customize their appearance and behavior.

## Features

- **Customizable Window**: Create a window with specified dimensions and title.
- **Widgets**: Add text, buttons, choice buttons, text fields, and radio group boxes.
- **Customization**: Customize widget properties such as text, size, alignment, and font.
- **Show/Hide**: Show or hide specific widgets or groups of widgets.
- **Moving Widgets**: Change the position of widgets within the window.

## Installation

1. Clone the repository using the following command:

    ```bash
    git clone https://github.com/maximnota/Enhanced-PyQT.git
    ```

2. Install the required dependencies:

    ```bash
    pip install PyQt5
    ```

## Usage

1. Initialize the `CustomWindow` object with specified dimensions and title.
2. Write the `create()` method
3. Use various methods provided by `CustomWindow` class to add widgets, customize them, show/hide, and manipulate their properties.
4. Run the application using the `init()` method.

Example:

```python
from CustomWindow import CustomWindow

# Create a CustomWindow object
window = CustomWindow(500, 600, "My Custom Window")
window.create()

# Add widgets, customize them, and perform operations

# Initialize the application
window.init()
```

## Documentation

### `CustomWindow` Class

#### Methods

- `create()`: Creates the main window.
- `addChoiceButton(buttonName, function)`: Adds a choice button to the window.
- `addButton(buttonName, function)`: Adds a button to the window.
- `addText(text, textSize, Alignment)`: Adds text to the window.
- `addTextField(height, width, Alignment)`: Adds a text field to the window.
- `getTextFieldValue(ID)`: Retrieves the value from a text field.
- `HideAll()`: Hides all widgets.
- `ShowAll()`: Shows all widgets.
- `HideObject(objectType, objectID)`: Hides a specific widget.
- `ShowObject(objectType, objectID)`: Shows a specific widget.
- `changeText(ID, Text)`: Changes the text of a widget.
- `changeFont(objectType, ID, customFont, Size)`: Changes the font of a widget.
- `move(new_x, new_y, objectID, objectType)`: Moves a widget to a new position.
- `addImage(image_path, width, height)`: creates an image
- `changeImage(objectID, image_path, width, height)`: changes the image value of an image widget
- `changeColor(objectType, ID, color)`: Changes the color of a widget
- `addTextBorder(objectID, thickness, style, color)`: creates a border for a text label
- `changeWindowOpacity(newOpacity)`: Changes the window opacity
- `changeWindowTitle(newTitle)`: Changes the title of the window
- `init()`: Initializes and runs the application.
  ### `BasicWindow` Class

The `BasicWindow` class creates a simple window for displaying content.

#### Methods

- `printInfo()`: Prints information about the window (height, width, title).
- `create()`: Creates and displays the basic window.
- `hide()`: Hides the basic window.
## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements, bug fixes, or new features.
