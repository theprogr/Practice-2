n = int(input())
arr = list(map(int, input().split()))

mx = -1e9 - 5
pos = 0

for i in range(len(arr)):
    if arr[i] > mx:
        mx = arr[i]
        pos = i

print(pos + 1)