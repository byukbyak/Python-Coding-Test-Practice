n, x = map(int, input().split())
a = list(map(int, input().split()))
res = []
for i in a:
    if i < x:
        res.append(i)

print(" ".join(map(str, res)))