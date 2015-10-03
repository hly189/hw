def factorial(n): 
	if n == 0: 
		return 1
	else: 
		return n*factorial(n-1)

def sum(n): 
	if n==0: 
		return 0
	else: 
		return n + sum(n-1)

def ab_plus_c(a,b,c):  
	if b==0: 
		return c
	else: 
		return a + ab_plus_c(a, b-1,c)

def square(x): 
	return x*x

def summation(n, term): 
	"""
	>>> summation(3, square)
	14
	"""
	if n==0: 
		return term(0)
	else: 
		return term(n) + summation(n-1, term)

def hailstone(n): 
	i = 0
	print(n)
	while n != 1: 
		if n%2==0: 
			n = n//2
		else: 
			n = n*3+1
		i = i +1
		print(n)
	return i + 1

def hailstone2(n): 
	print(n)
	
	if n==1: 
		
		return
	if n%2==0: 
		return hailstone2(n//2)
		
	else: 
		return hailstone2(n*3+1)

def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n): 
 	if n==0: 
 		return lambda x: x
 	else: 
 		return compose1(f, repeated(f, n - 1))

def factorial(n): 
	i, total = 0, 1
	if n==0: 
		return 1
	else: 
		while i < n: 
			total = total*(i+1)
			i = i +1
		return total

def falling(n, k):
    """
    Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    """
    total, i = 1, 0
    if k==0: 
    	return 1
    else: 
    	while i < k: 
    		total = total * n 
    		n = n-1
    		i = i+1
    	return total 

def falling2(n, k):
    """
    Compute the falling factorial of n to depth k.

    >>> falling2(6, 3)  # 6 * 5 * 4
    120
    >>> falling2(4, 0)
    1
    """
    if k==0: 
    	return 1
    else: 
    	return n * falling2(n-1, k-1)