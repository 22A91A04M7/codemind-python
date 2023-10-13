n=int(input())
sum=0
li=list(map(int,input().split()))
for i in li:
    if i%2!=0:
        sum=sum+i
print(sum)