def lis(lst):
	if nums == []:
		return 0

	table = [1]*len(nums)
	max_count = 1
	for i in range(len(nums)):
		for j in range(i):
			if nums[j] < nums[i] and table[j] + 1 > table[i]:
				table[i] = table[j] + 1
				max_count = max(max_count, table[i])
	return max_count

assert lis([1, 1, 2, 3, 1, 6, 8, 7, 9]) == 6