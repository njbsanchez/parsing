"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring, new_string = ""):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    if astring:
        new_string = new_string + astring[-1]
        astring = astring[:-1]
        return rev_string(astring, new_string)
    
    return new_string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
