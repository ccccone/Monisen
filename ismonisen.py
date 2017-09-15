import math
def ismonisen(m):
	if isprime(math.log(m+1, 2)) and isprime(m):
		return True
	return False
