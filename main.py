import isprime
import ismonisen

def main(n):
	if n!= int(n) or n<1:
		return []
	x = 3
	result = [3]
	while True:
		if isprime.isprime(x) and isprime.isprime(2**x - 1):
			result.append(2**x-1)
		if len(result) == n:
			return result[n-1]
		x += 2

print(main(int(input('please input a integer\n'))))