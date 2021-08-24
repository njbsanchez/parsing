<h1>Parsing Arrays</h1>

Compilation of all array whiteboarding problems with psuedocode notes and step by step guidance on how I solve each problem.

## Table of Contents

<li><a href="#diagonal_traverse">Diagonal Traverse</a></li>

<a name="diagonal traverse"></a>
## Diagonal Traverse

<p> Time Complexity: O(N * M) </p>
<p> Space Complexity O(min(N,M))</p>

1) base case - if matrix is empty, return matrix
2) create length and height variable for matrix size
3) create empty lists for result and intermediate (diagonal tracker)
4) create head_count (length + width - 1)
5) for loop through range of head count 
    - if else: track where to start
    - whole loop through diagonal (left, down)
        - add each item to intermediate list
    - if loop counter is even:
        - reverse intermediate list
    - append to result
    - clear intermediate
6) return result


