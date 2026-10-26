lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s1=lst[5:15:2]
s2=lst[::4]
sum=avg=0
print("slice 1")
for a in s1:
    sum+=a
    print(a,end='')
print()
print("sum of elements of slice 1:",sum)
print("slice2")
sum=0
for a in s2:
    sum+=a
    print(a,end='')
print()
avg=sum/len(s2)
print("average of elements of slice 2:",avg)


