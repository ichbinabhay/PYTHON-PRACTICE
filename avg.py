l=eval(input("enter a number"))
sum=avg=0
le=len(l)
for i in range(0,le):
    sum+=l[i]
    avg=sum/le
print("avg is ",avg)       