"""
HJKAI - Example Python Library
A simple AI math + logic library.

Author: HJK Inc.
License: HJK Inc. License
"""

# --- Core functions ---
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def theorem_pythagoras(a, b):
    """Returns the hypotenuse of a right triangle."""
    return (a**2 + b**2) ** 0.5


# --- Metadata for PyPI ---
__version__ = "0.1.0"
__author__ = "HJK Inc."
__license__ = "HJK Inc. License"


# --- Entry point ---
if __name__ == "__main__":
    print("HJKAI Library v", __version__)
    print("Example: theorem_pythagoras(3,4) =", theorem_pythagoras(3,4))
