from double_linked_list import DoubleLinkedList


def get_double_linked_list(items):
    linked_list = DoubleLinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list
