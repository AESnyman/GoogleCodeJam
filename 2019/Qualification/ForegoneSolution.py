# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231?show=progress


def calculate(n):
    x = 0
    y = 0
    for i in range(0,len(n)):
        if int(n[i]) == 4:
            x = x*10 + 2
            y = y*10 + 2
        else:
            x = x*10 + int(n[i])
            y = y*10
    return x, y
        


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer

for i in range(1, t + 1):
    n = input()
    x, y = calculate(n)

    print("Case #{}: {} {}".format(i, x, y))
    
  