l=[99,98,98,99,98,97,98,99,96,95,87,98,97,96]
s1=l[0::4]
print(s1)
sum=avg=0
for a in s1:
    sum+=a
    print(a,end='')
avg=sum/len(s1)
print("average of slice 1 is ",avg)


