"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for c in items:
        frequencies[str(c)] = 1 + frequencies.get(str(c),0)



    # Your code goes here
    return frequencies
