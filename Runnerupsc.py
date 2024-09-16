n=int(input("Enter the number of paricipant's scores: "))
L = list(map(int, input("Enter the scores: ").split()))[:n]
L.sort()
while(True):
    if(L[n-2]!=L[n-1]):
        print("The runner up score is: ",L[n-2])
        break
    n=n-1
