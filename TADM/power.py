def power(a, b):
	if b == 0:
		return 1

	if b % 2 == 0:
		c = power(a, b/2)
		return c*c
		
	c = power(a, b-1)
	return a*c

assert power(5, 0) == 1
assert power(17, 1) == 17
assert power(2, 28) == 268435456
assert power(3, 13) == 1594323