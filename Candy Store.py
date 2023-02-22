t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x >= y:
        print(y)
    else:
        r = y - x
        print(x+2*r)