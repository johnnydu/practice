def insertion_sort(lst):
	# iterate through list
	for i in range(len(lst)):
		j = i
		# while jth value out of place, swap down
		while j > 0 and lst[j] < lst[j-1]:
			lst[j], lst[j-1] = lst[j-1], lst[j]
			j -= 1

	return lst

assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([5,2,3,4,1]) == [1,2,3,4,5]
assert insertion_sort(list('hello world')) == sorted('hello world')
assert insertion_sort(list('insertion sort')) == sorted('insertion sort')