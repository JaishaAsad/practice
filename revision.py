# days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# for day in days:
#     if day == "sunday":
#         print ("It's holiday")
#     else:
#         print ("your have to go to work")
# # if we want to use slicing
# element = days [2:4]
# print (element)
# # del days [1]
# # print (days)
# a=days.pop()
# print (a)

#below we are working for tuple
days = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print (days)
print(days[1])
days = list (days)
days[0]='sunday'
print (days)
days= tuple (days)
print (days)
for day in range(0,len(days)):
    if days[day] == "sunday" : 
        print("Today is holiday")
    else:
        print("you have to work today")