n = int(input())
blank = " "
star = "*"
for i in range(1, n+1):
    print((blank*(n-i))+(star*i))