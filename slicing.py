# lst = [1,3,4,0,13,2]
# new_lst=[lst[2],lst[3],lst[4]]
# print(new_lst)
# new_lst2= []
# for i in range (2,5)
#     new_lst2.append(lst[i])
# print (new_lst2)
# print(lst[2:5])
lst=[2,3,4,5]
lst2=lst
lst2.append(20)
print(lst2)
print(lst)

a=10
b=a
b=20
print(a)
lst3=lst2[:]
print (lst3)
lst.append(45)
print(lst3)
print(lst2)
print(lst2[4::-1])
