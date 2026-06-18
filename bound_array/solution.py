import os
import sys

#sys.path.append(os.path.abspath('/usr/src/app/'))

from LinkedList import LinkedList
from .helpers import get_linked_list_from_array

def solution(t):
    print(t)


items = [[10, 20], 0, -1, ['hey']]

solution(items) # [['hey'], -1, 0, [10, 20]]
solution([]) # []