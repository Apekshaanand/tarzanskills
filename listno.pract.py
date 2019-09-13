
a=['cat','bat',7,8,100,-1,True,False]
d={}
for i in a:

    if str(type(i).__name__) not in d.keys():
        d[str(type(i).__name__)]=[i]
    else:
       d[str(type(i).__name__)].append(i)

print(d)