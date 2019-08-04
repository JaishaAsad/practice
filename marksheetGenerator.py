print ("please mention your name below:")
Name= input()
print ("please write down your class:")
clas= input()
print ("please enter your seat number:")
seatnum= input()
print("please enter your institute name:")
institutename= input()

print  ("-----------------------")
 
print ("MARKS")

print ("please mention your subject1 marks here:")
subject1=int (input ())
print ("please mention your subject2 marks here:")
subject2=int (input ())
print ("please mention your subject3 marks here:")
subject3= int (input ())
print ("please mention your subject4 marks here:")
subject4= int (input ())




print ("name:"+ Name)
print ("clas:"+clas)
print ("seatnum:"+seatnum)
print ("institutename:"+institutename)

print ("-----------")

print ("MARKS")

print ("subject1:"+str (subject1))
print ("subject2:"+ str (subject2))
print ("subject3:"+ str(subject3))
print ("subject4:"+str (subject4))


print ("------------------------")

totalmarks=subject1+subject2+subject3+subject4
percentage=totalmarks/400*100

print ("totalmarks:"+str(totalmarks))
print ("percentage:"+str (percentage)+"%")