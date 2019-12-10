A=[19,10,12,10,24,25,22]
temp=set()
temp.add(A[0])
my_set_list=[]
my_set_list.append(temp)
print(temp)
print(my_set_list)
k=4
for ele in A[1:]:
    print("Next Ele", ele)
    for Set in my_set_list:
        x=set()
        for ele_Set in Set:
            if (ele +  ele_Set) % k !=0:
                x.add(ele)
                x.add(ele_Set)
            input()
            print("Element from Set", ele_Set)
            print(x)
    my_set_list.append(x)
    print(my_set_list)
