lst=eval(input("enter a list:"))
ln=len(lst)
mx=max(lst)
ind=lst.index(mx)
if ind<=(ln/2):
    print("The maximum element",mx,"lies in the first half.")
else:
    print("The maximum element",mx,"lies in the 2nd half")    