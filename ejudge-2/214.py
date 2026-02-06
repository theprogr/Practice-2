n = int(input())
arr = list(map(int, input().split()))
arr.sort()

my_dict = {}
for i in arr:
    my_dict[i] = my_dict.get(i, 0) + 1 

mx = 0
ans = 0
for i in my_dict:
    if my_dict[i] > mx:
        mx = my_dict[i]
        ans = i

print(ans)