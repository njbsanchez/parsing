def findDiagonalOrder(self, matrix):
    
    if not matrix or not matrix[0]:
        return []

    length, height, result, intermediate = len(matrix), len(matrix[0]), [], []

    head_count = length + height - 1
    
    for cur in range(head_count):

        if cur < height:                                                
            x = 0
        else: 
            x = cur - height + 1
        
        if cur < length:
            y = cur
        else:
            y = height - 1
                                        
        while x < length and y > -1:
            intermediate.append(matrix[x][y])
            x += 1
            y -= 1

        if cur % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
        
        intermediate = []            
                                                
    return result        