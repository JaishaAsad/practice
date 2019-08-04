user_input = float (input("enter your CGPA:"))
if  user_input >= 3.7:
    print ("your grade is A+")
elif user_input< 3.7 and user_input>=3.5:
    print ("your grade is A")
elif user_input<3.5 and user_input>=3.0:
    print ("your grade is B")
elif user_input<3.0 and user_input>=2.5:
     print ("your grade is C")
else: user_input<2.5 and user_input>=0:
    print ("Sorry you are fail")