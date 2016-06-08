"""

Extremely imperfect function that attempts to find all factors of a provided number
Examples of long-to-calculate: 1444141111111

Examples of short-to-calculate: 1444141111112, 65535

Very much a work-in-progress; not guaranteed to be correct, accurate or even efficient.

"""

def findFactorsOf(n):
	maxToCheck = (n / 2) + 1
	found = [1, n]
	i = 3
	incrementer = 1 if n % 2 == 0 else 2
	while i < maxToCheck:
		if n % i == 0:
			found.append(i)
			found.append(n / i)
			print found # remove or do at end if you just want the result
			maxToCheck = (n / i)
		i = i + incrementer
	return found

def isPrime(n):
	maxToCheck = (n / 2) + 1
	i = 3
	if n % 2 == 0: return False

	while i < maxToCheck:
		if n % i == 0:
			return False
		i = i + 2
	return True


factors = findFactorsOf(1444141111112)
primeFactors = []
for num in factors[2:]:
	if isPrime(num):
		print num
