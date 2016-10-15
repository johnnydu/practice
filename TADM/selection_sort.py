def selection_sort(lst):
	for i in range(len(lst)):
		min_index = -1
		for j in range(i, len(lst)):
			if min_index == -1 or lst[j] < lst[min_index]:
				min_index = j
		lst[i], lst[min_index] = lst[min_index], lst[i]
	return lst

assert selection_sort([1,14,52,2,31,31,61,6]) == [1, 2, 6, 14, 31, 31, 52, 61]
assert selection_sort([]) == []
assert selection_sort([1]) == [1]