def movie_scheduling(intervals):
	sorted_by_completion = sorted(intervals, key=lambda i: i[1])
	result = []
	last_completion = 0
	for i in range(len(sorted_by_completion)):
		start_time, end_time = sorted_by_completion[i]
		if start_time >= last_completion:
			last_completion = end_time
			result.append(sorted_by_completion[i])
	return result

print movie_scheduling([(1,5), (4,6), (5,10)])

