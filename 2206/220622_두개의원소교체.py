n, k = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(n, k, a, b):
    a.sort()
    b.sort(reverse = True)

    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break

    return sum(a)

print(solve(n, k, a, b))