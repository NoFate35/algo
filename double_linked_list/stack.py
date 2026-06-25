def edit(string):
	edit_string = []
	for i in string:
		if i == '#':
			edit_string.pop()
		else:
			edit_string.append(i)
	return edit_string


def solution(first, second):
	edit_first = edit(first)
	edit_second = edit(second)
	return edit_first == edit_second

solution('ab#c', 'ab#c'); # True
solution('ab##', 'c#d#'); # True
solution('a#c', 'b'); # False