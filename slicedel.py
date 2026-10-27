val=[17,23,28,19]
print("The list is:",val)
print("Deletion menu")
print("1.Delete using value")
print("2.Delete using index")
print("3.Delete a sublist")
dch=int(input("enter choice"))
if dch == 1 :
    item=int(input("enter item to be deleted:"))
    val.remove(item)
    print("list now is:",val)
elif dch==2 :
    index=int(input("index of item to be deleted:"))
    val.pop(index)
    print("List now is:",val)
elif dch==3 :
    l=int(input("lower limit of list slice:"))
    h=int(input("Upper limit of list slice:")) 
    del val[l:h]
    print("list now is:",val)
else:
    print("valid choices are 1/2/3 only")
    






