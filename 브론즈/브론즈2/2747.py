n = int(input())

a = 0
b = 1
for i in range(2, n + 1):
    a, b = b, a + b

print(b)