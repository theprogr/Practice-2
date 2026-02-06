n = int(input())
arr = list(map(int, input().split()))
ans = -1e9 - 5

for i in arr:
    ans = max(ans, i)

print(ans)