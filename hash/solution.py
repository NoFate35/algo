import os
import sys

print(sys.path)

from Hash import Hash  # noqa: E402

def remove(hash, key):
    print('hash', hash, 'key', key)

def solution(map, key):
    hash = Hash()

    for key_, value in map.items():
        hash.set(key_, value)

    return remove(hash, key)


table = Hash()
table.set("key", "value")
table.set("key1", "value1")

removed = solution(table, "key")
#print(removed)  # => value

# В хеше ключа больше нет
table.get("key")  # None