n = int(input())

my_dict = {}

for i in range(n):
    s = input()
    my_dict[s] = my_dict.get(s, 0) + 1

ans = 0
for key in my_dict:
    if my_dict[key] == 3:
        ans += 1

print(ans)