def solution(a, b):
	a = abs(a)
	b = abs(b)
	if a == b:
		return a
	elif a > b:
		return solution(a - b, b)
	else:
		return solution(a, b - a)
print(solution(38, 28)) # => 2
print(solution(129, 90)) # => 3