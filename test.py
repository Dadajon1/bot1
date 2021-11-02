a = input().split(" ")
b = []
for i in a:
    b.append(int(i))
print(*sorted(b))