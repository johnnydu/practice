def power_set(lst):
	if lst == []:
		return [[]]

	without = power_set(lst[1:])
	with_first = [[lst[0]] + rest for rest in without]
	return without + with_first

print power_set(range(3))