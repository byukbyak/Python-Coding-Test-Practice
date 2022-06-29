arr = [1,2,3,2,5]
count = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print("arr : ", arr[i:j+1])
        print("sum : ", sum(arr[i:j+1]))
        if sum(arr[i:j+1]) == 5:
            count += 1
print(count)