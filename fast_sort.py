def partition(items, left, right, pivot):
    while True:
        while items[left] < pivot:
            left += 1

        while items[right] > pivot:
            right -= 1

        if left >= right:
            return right + 1

        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

def partitionr(items, left, right, pivot):
    while True:
        while items[left] > pivot:
            left += 1

        while items[right] < pivot:
            right -= 1

        if left >= right:
            return right + 1

        items[right], items[left] = items[left], items[right]
        left += 1
        right -= 1


def solution(items, rev='asc'):
    left = 0
    right = len(items) - 1
    sorted(items, left, right, rev)
    return print(items)

def sorted(items, left, right, rev):
    length = right - left + 1

    if length < 2:
        return

    pivot = items[left]
    if rev == 'desc':
        split_index = partitionr(items, left, right, pivot)
    else:
        split_index = partition(items, left, right, pivot)
    sorted(items, left, split_index - 1, rev)
    sorted(items, split_index, right, rev)





items = [10, 20, 0, -1]

solution(items) # [-1, 0, 10, 20]
solution([]) # []
solution(items, 'desc') # [20, 10, 0, -1]