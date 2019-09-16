list=[]
no_of_input = int(input("Enter the nunber you want : "))
for i in range(0,no_of_input):
    score_list=int(input("Enter the score : "))
    list.append(i)
list.sort()
print(list[-2])