# 평가 입력받아 다르게 출력하기(py)

# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# others : what?

c = str(input())

if c in 'A':
    print('best!!!')
elif c in 'B':
    print('good!!')
elif c in 'C':
    print('run!')
elif c in 'D':
    print('slowly~')
else:
    print('what?')
