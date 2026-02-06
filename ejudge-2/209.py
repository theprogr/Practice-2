n = int(input())
arr = list(map(int, input().split()))

mx = -1e9 - 5
mn = 1e9 + 5

for i in arr:
    mx = max(mx, i)
    mn = min(mn, i)

for i in arr:
    if i == mx:
        i = mn
    print(i, end=" ")