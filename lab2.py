def abs(x): 
	if x>=0: 
		return x
	return -x

def foo(x):
	if x > 0: 
		print("greater than zero")
	print("less than zero")

def exp_decay(n): 
	if n%2 != 0: 
		return
	while n > 0: 
		print(n)
		n = n //2


def funky(k):
	while k < 50: 
		if k %2==0: 
			k += 13
		else: 
			k +=1
		print(k)
	return k 

def factorial(n): 
	k = n; 
	while k <= n: 
		if n%k == 0: 
			print(k)
			k = k -1
		else: 
			k = k-1
	return

def divide(num, divisor):
    """
    >>> divide(8, 2)
    4
    """
    i = 0
    while i < divisor: 
    	num = num - divisor
    	i +=1
    return num

def square(x):
   return x*x

def neg(f,x): 
 	return -f(x)

def first(x): 
	x += 8
	def second(y): 
		print('second')
		return x + y
	print('first')
	return second

def troy(): 
	abed = 0
	while abed < 10: 
		def britta(): 
			return abed
		abed +=1
	abed = 20
	return britta

annie = troy()

def shirley(): 
	return annie

pierce = shirley()


