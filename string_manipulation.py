def count_vowels(str):
    """
    >>> count_vowels("hello")
    2
    """
    vowels = set(["a","e", "i", "o", "u"])
    counter = 0
    for char in str:
        if char in vowels:
            counter += 1
    return counter
    
def reverse_str(str):
    """
    >>> reverse_str("hello")
    'olleh'
    """
    answer = []
    for i in range(len(str)-1, -1, -1):
        answer.append(str[i])
    return "".join(answer)
    
def reverse_sentence(str):
    """
    >>> reverse_sentence("i am great")
    'great am i'
    """
    answer = []
    str_lst = str.split(" ")
    for i in range(len(str_lst)-1, -1, -1):
        answer.append(str_lst[i])
    return " ".join(answer)

def remove_dup(str):
    """
    >>> remove_dup("abbcdefgg")
    'abcdefg'
    """
    answer = []
    dup_set = set()
    for char in str:
        if char not in dup_set:
            answer.append(char)
            dup_set.add(char)
    return "".join(answer)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
