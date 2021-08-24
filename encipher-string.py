"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    new_string = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = [let for let in alpha]
    upper_list = [let for let in upper]
     
    for char in txt:
        if char.isalpha():
            if char.isupper():
                char_indx = upper_list.index(char)     #is a number
                new_string.append(upper_list[char_indx - (26 - shift)])
            else:
                char_indx = alpha_list.index(char)     #is a number
                new_string.append(alpha_list[char_indx - (26 - shift)])
        else: new_string.append(char)
    
    return "".join(new_string)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
