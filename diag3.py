def if_this_not_that(i_list, this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    i = 0
    while i < len(i_list): 
    	if i_list[i] <= this: 
    		print("that")
    	else: 
    		print(i_list[i])
    	i+=1

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a list of sequences, each
    corresponding to a group.

    >>> group(range(14))
    [range(0, 4), range(4, 9), range(9, 14)]
    >>> group(list(range(17)))
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15, 16]]
    """
    num = len(seq)
    assert num >= 12
    if num == 12 or num == 13: 
    	return [seq[:4], seq[4:8], seq[8:]]
    elif num == 14: 
    	return [seq[:4], seq[4:9], seq[9:]]
    elif num == 15: 
    	return [seq[:5], seq[5:10], seq[10:]]
    return [seq[:4]] + group(seq[4:])

def filter_link(predicate, r):
    """ Returns a link only containing elements in r that satisfy
    predicate.

    >>> r = link(25, link(5, link(50, link(49, empty)))))
    >>> new = filter_link(lambda x : x % 2 == 0, r))
    >>> first(new)
    50
    >>> rest(new) == empty_link
    True
    """
    if r == empty:
    	return r
    elif predicate(first(r)): 
    	return link(first(r), filter_link(predicate, rest(r)))
    else: 
    	return filter_link(predicate, rest(r))


def reverse_iterative(s):
    """Return a reversed version of a linked list s.

    >>> primes = link(2, link(3, link(5, link(7, empty))))
    >>> reverse_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    rev_list = empty
    while s != empty:
        rev_list = link(first(s), rev_list)
        s = rest(s)
    return rev_list

# Linked List definition
empty = None

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)
