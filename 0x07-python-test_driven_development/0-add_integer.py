#!/usr/bin/python3
"""
Shebang Line Documentation:

This script uses Python 3. Ensure the correct interpreter path:

    #!/usr/bin/python3

Update the path if needed. Example:

    #!/usr/local/bin/python3
"""
"""
Module for add_integer method.
"""
def add_integer(a, b=98):
    """
    Add Integer Function:

    Adds two integers, 'a' and 'b', and returns the result.

    Parameters:
    - a (int): The first integer.
    - b (int, optional): The second integer. Default is 98.

    Returns:
    int: The sum of 'a' and 'b'.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
        return
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
        return
return int (a) + int (b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
