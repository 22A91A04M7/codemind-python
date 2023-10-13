n=int(input())
li=list(map(int,input().split()))
a=sum(li)//n
if a in li:
    print("True")
else:
    print("False")