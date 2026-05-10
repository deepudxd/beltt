"""
utils/strings.py
String utility functions for Our package will go in this file.
"""

"""
Init: create a functino which reverses order of words in a given string.

example: 
    Input -> "Hello Iam A Farmer"
    Output -> "Farmer A Iam Hello"

Function Name: reverse_words()
Input Attributes: [ text: str ]
Output: str
"""

def reverse_words(text: str) -> str:
    words = text.split()
    reversed_text = " ".join(words[::-1])
    return reversed_text
