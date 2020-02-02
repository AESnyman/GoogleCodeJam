# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da?show=progress


def calculate(moves):
    s = ''
    for m in moves:
        if m == 'S':
            s = s+'E'
        else:
            s = s+'S'

    return s

t = int(input()) 
for i in range(1, t + 1):
    n = int( input())
    moves = input() # read a list of integers, 2 in this case
    s = calculate(list(moves))

    print("Case #{}: {}".format(i, str(s) ) )