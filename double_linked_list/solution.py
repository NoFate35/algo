from double_linked_list_node import DoubleLinkedListNode  # noqa: E402
from helpers import get_double_linked_list

def solution(items):
    print(items)

items = [[10, 20], 0, -1, ['hey']]

solution(items) # [0, [10, 20], -1, ['hey']]
solution([]) # []