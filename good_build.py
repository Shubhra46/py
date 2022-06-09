N=int(input())
H=list(map(int,input().strip().split()))[:N]
count=[]

        
for i in range(0,N-1):
    temp=H[i]
    a=0
    for j in range(i+1,N):
        if temp >= H[j]:
            a+=1
            
    if a== N-1-i:
        count.append(temp)
        
count.append(H[N-1])   

print(" ".join(map(str,count)))