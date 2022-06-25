num = int(input())
sum = 0
result = 0
for i in range(num):
    if sum >= num:
        break
    else:
        sum += i
        result = i
print(result)