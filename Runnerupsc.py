n=int(input())
L = list(map(int, input().split()))[:n]
L.sort()
while(True):
    if(L[n-2]!=L[n-1]):
        print(L[n-2])
        break
    n=n-1
