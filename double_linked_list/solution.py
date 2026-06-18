from double_linked_list_node import DoubleLinkedListNode  # noqa: E402
from helpers import get_double_linked_list

def solution(items):
    if items == []:
        return items
    del_value = items[1]
    double_linked_list = get_double_linked_list(items)
    deleted_to_first_node = double_linked_list.delete(del_value)
    double_linked_list.prepend(deleted_to_first_node.value)
    return double_linked_list.to_array()

items = [[10, 20], 0, -1, ['hey']]

solution(items) # [0, [10, 20], -1, ['hey']]
solution([]) # []
solution([1, 2, 1, 1, 1, 2]) #[2, 1, 1, 1, 1, 2]