a=[11,45,8,11,23,45,23,45,89]
b={}
for value in a:
    count=0
    for value1 in a:
        if value==value1:
            count+=1

    b[value]=count
print(b)



