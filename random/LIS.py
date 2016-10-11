def lis(lst):
	if lst == []:
		return 0

	table = [1]*len(lst)
	max_count = 1
	for i in range(len(lst)):
		for j in range(i):
			if lst[j] < lst[i] and table[j] + 1 > table[i]:
				table[i] = table[j] + 1
				max_count = max(max_count, table[i])
	return max_count

assert lis([1, 1, 2, 3, 1, 6, 8, 7, 9]) == 6
assert lis([]) == 0
assert lis([1]) == 1
assert lis([2, 1]) == 1
assert lis([1, 3, 2, 5]) == 3