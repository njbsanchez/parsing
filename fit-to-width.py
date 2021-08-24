"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""
    
    print_phrase = []
    line_to_add = ""
    words = string.split(" ")
    
    for word in words:
        if len(line_to_add) == 0:
            line_to_add = word
        elif len(word) + len(line_to_add) >= limit:
            print_phrase.append(line_to_add)
            line_to_add = word
        else:
            line_to_add += " " + word
    
    print_phrase.append(line_to_add)
    
    for line in print_phrase:
        print(line)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
