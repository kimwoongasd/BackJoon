# python
n = int(input())

dp = [x for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        else:
            if dp[i] > dp[i - j * j] + 1:
                dp[i] = dp[i - j * j] + 1

print(dp[n])


# pyp3 시간초과 안남
# n = int(input())

# dp = [x for x in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, i):
#         if j * j > n:
#             break
#         else:
#             if dp[i] > dp[i - j * j] + 1:
#                 dp[i] = dp[i - j * j] + 1

# print(dp[n])