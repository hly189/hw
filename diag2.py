def summation(n, term): 
    """Return the sum of the 0th to nth terms in the sequence defined
    by term.
    Should be implemented using recursion.

    >>> summation(5, lambda x: x * x * x)
    225
    >>> summation(9, lambda x: x + 1)
    55
    >>> summation(5, lambda x: 2**x)
    63
    """
    if n == 0: 
        return term(0)
    else: 
        return term(n) + summation(n-1, term)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k %10 == 7: 
        return True
    elif k < 10: 
        return False
    else: 
        return has_seven(k//10)

def iterative_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(iterative_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(iterative_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    i = k
    result = 0
    while i >= 1: 
        result = n_term(i)/(d_term(i)+result)
        i = i-1
    return result                     

def recursive_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(recursive_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(recursive_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    def helper(n_temr, d_term, k, i): 
        denom = d_term(i)
        if i < k: 
            denom += helper(n_term, d_term, k, i+1)
        return n_term(i)/denom
    return helper(n_term, d_term, k, 1)

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    >>> part(10)
    42
    >>> part(15)
    176
    >>> part(20)
    627
    """
    def helper(n,m): 
        if n < 0 or m <=0: 
            return 0
        if n==0: 
            return 1
        else: 
            return helper(n-m,m) + helper(n,m-1)
    return helper(n,n)
