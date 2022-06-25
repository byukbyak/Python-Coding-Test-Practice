s = input()
n = 0
if s == 'A': n = 10
elif s == 'B': n = 11
elif s == 'C': n = 12
elif s == 'D': n = 13
elif s == 'E': n = 14
elif s == 'F': n = 15

for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')