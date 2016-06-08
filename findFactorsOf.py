"""

Extremely imperfect function that attempts to find all factors of a provided number
Examples of long-to-calculate: 1444141111111

Examples of short-to-calculate: 1444141111112, 65535

Very much a work-in-progress; not guaranteed to be correct, accurate or even efficient.

"""

def findFactorsOf(n):
	maxToCheck = (n / 2) + 1
	found = []
	i = 1
	incrementer = 1 if n % 2 == 0 else 2
	while i < maxToCheck:
		if n % i == 0:
			found.append(i)
			found.append(n / i)
			print found # remove or do at end if you just want the result
			maxToCheck = (n / i)
		i = i + incrementer

findFactorsOf(65535)
