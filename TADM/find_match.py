def find_match(pattern, text):
	for i in range(len(text)-len(pattern)+1):
		j = 0
		while j < len(pattern) and pattern[j] == text[i+j]:
			j += 1
		if j == len(pattern):
			return i
	return -1

assert find_match('abba', 'aababba') == 3
assert  find_match('ab', 'ba') == -1
assert find_match('', 'abb') == 0
assert find_match('ab', '') == -1
assert find_match('ad', 'add') == 0
assert find_match('addd', 'add') == -1