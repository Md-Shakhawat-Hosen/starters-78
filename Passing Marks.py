t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    li = list(map(int,input().split()))[:n]
    li.sort(reverse=True)
    print(li[x-1]-1)