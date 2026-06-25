from double_linked_list_node import DoubleLinkedListNode  # noqa: E402
from helpers import get_double_linked_list

def solution(items):
    if len(items) < 2:
        return items
    first_value = items.pop(0)
    sec_value = items.pop(0)
    items.insert(0, first_value)
    items.insert(0, sec_value)
    return items

items = [[10, 20], 0, -1, ['hey']]

solution(items) # [0, [10, 20], -1, ['hey']]
solution([]) # []
solution([1, 2, 1, 1, 1, 2]) #[2, 1, 1, 1, 1, 2]