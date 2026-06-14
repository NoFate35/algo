def numb(name, bookd):
	for i in bookd:
		if i['name'] == name:
			return i['number']

def solution(bookd, name):
	if bookd == []:
		return 'Phonebook is empty!'
	names = sorted([i['name'] for i in bookd])
	print('names', names)
	first = 0
	last = len(names) - 1
	while (first <= last):
		middle = (first + last) // 2
		if name == names[middle]:
			return numb(name, bookd)
		if name < names[middle]:
			last = middle - 1
		else:
			first = middle + 1
	return "Name not found!"

"""
listt = [i for i in range(1, 129)]
solution(listt, 6)
"""

phonebook = [
  {'name': 'Alex Bowman', 'number': '48-2002'},
  {'name': 'Aric Almirola', 'number': '10-1001'},
  {'name': 'Bubba Wallace', 'number': '23-1111'},
]
#print("book", [i['name'] for i in phonebook])

print(solution(phonebook, 'Alex Bowman'))# '48-2002'
print(solution(phonebook, 'None')) # 'Name not found!'
print(solution([], 'Alex Bowman')) # 'Phonebook is empty!'
