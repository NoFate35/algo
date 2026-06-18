import os
import sys
#print('sys.path', sys.path)
#sys.path.append(os.path.abspath('/usr/src/app/'))

from LinkedList import LinkedList
from helpers import get_linked_list_from_array

def solution(t):
    linked_list = get_linked_list_from_array(t[::-1])
    array = linked_list.to_array()
    print('ll', array)

'''
def solution(items):
    linked_list = get_linked_list_from_array(items)
    reversed_list = LinkedList()

    if not linked_list.head:
        return reversed_list.to_array()

    reversed_list.prepend(linked_list.head.value)
    next_node = linked_list.head.next
    while next_node:
        reversed_list.prepend(next_node.value)
        next_node = next_node.next
    return reversed_list.to_array()
'''

items = [[10, 20], 0, -1, ['hey']]

solution(items) # [['hey'], -1, 0, [10, 20]]
solution([]) # []