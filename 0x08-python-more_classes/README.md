# 0x08. Python - More Classes and Objects

Welcome to the "Python - More Classes and Objects" project! This series of tasks involves creating and manipulating a Rectangle class in Python. Each task builds upon the previous one, introducing new features and functionalities.

## Tasks

### Task 0: Simple Rectangle
Create an empty class `Rectangle` that defines a rectangle. No attributes or methods are required for this task.

### Task 1: Real Definition of a Rectangle
Define a `Rectangle` class with private attributes `width` and `height`. Implement setter and getter methods for both attributes. Allow instantiation with optional width and height.

### Task 2: Area and Perimeter
Enhance the `Rectangle` class to include methods for calculating the area and perimeter of the rectangle. Implement proper error handling for attribute values.

### Task 3: String Representation
Add a string representation to the `Rectangle` class using the `__str__` method. Customize the string representation to print the rectangle using the # character.

### Task 4: Eval is Magic
Implement the `__repr__` method in the `Rectangle` class to provide a string representation that can be used with the `eval` function to recreate a new instance.

### Task 5: Detect Instance Deletion
Add a `__del__` method to the `Rectangle` class to print a message when an instance of the rectangle is deleted.

### Task 6: How Many Instances
Introduce a class attribute `number_of_instances` in the `Rectangle` class to keep track of the number of instances created. Increment and decrement this attribute accordingly.

### Task 7: Change Representation
Enhance the `Rectangle` class to include a class attribute `print_symbol` for customizing the string representation. Update the `__str__` method to use this symbol.

### Task 8: Compare Rectangles
Implement a static method `bigger_or_equal` in the `Rectangle` class that compares two rectangles based on their area and returns the bigger one.

### Task 9: A Square is a Rectangle
Extend the `Rectangle` class with a class method `square` that creates a new instance with equal width and height, forming a square.

## Getting Started
To run the provided examples for each task, navigate to the corresponding file in the `0x08-python-more_classes` directory and execute the associated main file. For example:

```bash
./0-main.py
./1-main.py
# ... and so on

