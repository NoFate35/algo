import math

def solution(n):
    if n == 1:
        return False
    print(n)
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print(solution(1))
print(solution(2147483648))
print(solution(87178291199))