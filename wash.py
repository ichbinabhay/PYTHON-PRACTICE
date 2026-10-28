lst=eval(input("enter list of integer between 1 to 12:"))
length=len(lst)
for i in range(0,length):
    if lst[i]>10:
        lst[i]=10
print(lst)

