print ("please enter your subject 1 marks:")
subject1 = int(input())
print ("please enter your subject 2 marks:")
subject2 = int (input())
print ("please enter your subject 3 marks:")
subject3 = int (input())
print ("please enter your subject 4 marks:")
subject4 = int(input())

totalmarks =(subject1+subject2+subject3+subject4)
cgpa = totalmarks/400*3

print ("totalmarks:"+str(totalmarks))
print ("cgpa:" +str(cgpa))
