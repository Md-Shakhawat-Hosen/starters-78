t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    s = a + b
    if s > 6:
        print("YES")
    else:
        print("NO")