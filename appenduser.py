my=[11,22,33,44,55,66,77]
print("Exissting  list is:",my)
n=eval(input("enter a number or list to be appended"))
if type(n)==type([]):
    my.extend(n)
elif type(n)==type(1):
    my.append(n)
else:
    print("please enter either an integer or a list.")
print("Appended list is:",my)

