A, B = map(int, input().split())
C = int(input())
B += C

while B >= 60:
    A += 1
    B -= 60

A %= 24

print(A, B)
