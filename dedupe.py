"""Return new list from items with duplicates removed.

For example::

    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared::

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

A list with no duplicates would return the same::

    >>> deduped([1, 2, 3])
    [1, 2, 3]

This should return a *new* list, not mutate the existing
list::

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

An empty list should return an empty list::

    >>> deduped([])
    []

"""


def deduped(items):
    """Return new list from items with duplicates removed."""
    """
    
    test: deduped([1, 2, 1, 1, 3])
    
    create a dup_set
    create final_list
    for loop thru items_list
        if item not in dup_set
            append item to final list
            add item to dup_set
            
    return final_list
    
    """
    
    dup_set = set()
    final_lst = []
    
    for item in items:
        if item not in dup_set:
            final_lst.append(item)
            dup_set.add(item)
    
    return final_lst
    
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NO DUPE!\n")
