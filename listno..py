l = [100,200,1,0,-1,-7]
l.sort()
print(l[0],l[-1])



l=[1,2,3,1,1,4,5,6,6]
print(set(l))
print(list(set(l)))




a=[1,1,2,7]
b=[1,7,8,9]
print(list(set(a)))





l=[100,200,1,0,-1,-7]
length = len(l)
c=[]
d=[]
for i in l:

    if(i>=0):
        c.append(i)
    else:
        d.append(i)
        print(c,d)



a=['cat','bat',7,8,9,-7,True,False]
l=[]
j=[]
k=[]
for i in a:
    if type(i)==int:
        l.append(i)
    elif type(i)==str:
        j.append(i)
    elif type(i)==bool:
        k.append(i)
l.sort()
j.sort()
k.sort()
print(l,j,k)





a=['cat','bat',7,8,9,-7,True,False]

for i in a:
    if type(i)==int:l=[]
j=[]
k=[]
        l.append(i)
    elif type(i)==str:
        j.append(i)
    elif type(i)==bool:
        k.append(i)
l.sort()
j.sort()
k.sort()
dict={"int":l,"str":j,"bool":k}
print(dict)