n=int(input())
sum=0
li=list(map(int,input().split()))
for i in range(0,n):
    if i%2!=0:
        sum=sum+li[i]
print(sum)