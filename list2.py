list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]
list3 = []
def even_odd(list1,list2,list3):
    for i in list1:
        if i%2==0:
            list3.append(i)
    for j in list2:
        if j%2!=0:
            list3.append(j)


even_odd(list1,list2,list3)
print(list3)