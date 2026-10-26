lst=[10,12,14,20,22,24,30,32,34]
seq=lst[3:-3]
print(seq)
u=lst[3:8]
print(u)
p=lst[2:-2]
print(p)
r=lst[0:9:2]
print(r)
q=lst[0:9:3]
print(q)
t=lst[::3]
print(t)
w=lst[5::2]
print(w)
la=[11,12,13]
lb=la.copy()
print(lb)
la[0]+=10
la[-1]+=10
print(la)
print(len(la))
print(la.index(12))
la.append(17)
print(la)
colours=['red','blue','green']
colours.append('yellow')
print(colours)
la.extend(colours)
print(la)
colours.insert(2,'black')
print(colours)
colours.insert(len(colours),22)
print(colours)
colours.pop(2)
print(colours)
colours.remove('green')
print(colours)
colours.clear()
print(colours)





















