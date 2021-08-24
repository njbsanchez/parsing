"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3],[4, 5, 6],[7, 8, 9]])
    
    [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""

# """Pseudocode:
#         assumption - there is only 1 zeroo in entire matrix
        
#         get knowns:
        
#         # of rows = len(matrix)
#         # of columns = len(matrix[0])
        
#         row_to_update = ""
#         column_to_update = ""
        
#         for loop - row, row_lst in enumerate(matrix):
#             for loop - for column, row_item in enumerate(row_lst):
#                 if row_item is = 0:
#                     row_to_update = row
#                     column_to_update = column
#                     break
            
#         if row_to_update:
#             for idx, row in matrix:
#                 if idx = row_to_update:
#                     for column, row
                
#                     """

def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
    
#     ""
#     # of rows
#     # of columns
    
#     for loop thru rows - for indx, x in enumerate(matrix):
#         for loop through columns in rows - for indy, y in enumerate(x),
#             if y == 0:
#                 row_marker = indx
#                 column marker = indy
#                 break
    
#     if row_marker:
#         for loop thru rows - for indx, x in enumerate(matrix):
#             if indx == row_marker:
#                 for loop though columns = for y in x,
#                     y = 0
#             for loop through columns in rows - for indy, y in enumerate(x),
#                 if indy == column_marker:
#                     y = 0
    
#     return matrix    
    # """
    
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    
    row_marker = None
    column_marker = None
    
    for indx, x in enumerate(matrix):
        for indy, y in enumerate(x):
            if y == 0:
                row_marker = indx
                column_marker = indy
                break
    
    if row_marker == None:
        return None        
    for indx, x in enumerate(matrix):
        if indx == row_marker:
            for indy, y in enumerate(x):
                matrix[indx][indy] = 0
        for indy, y in enumerate(x):
            if indy == column_marker:
                matrix[indx][indy] = 0

    
    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
