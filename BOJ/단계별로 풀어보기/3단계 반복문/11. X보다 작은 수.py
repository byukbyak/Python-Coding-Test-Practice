n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(x):
    if i in a:
        pass
    else:
        a.remove(i+1)

print(sorted(a))