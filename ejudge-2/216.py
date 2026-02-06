n = int(input())
arr = list(map(int, input().split()))

my_dict = {}

for i in arr:
    if my_dict.get(i, 0) == 0:
        print("YES")
    else:
        print("NO")
    my_dict[i] = my_dict.get(i, 0) + 1