print ("please enter your english marks:")
englishmarks = int(input())
print ("please enter your urdu marks:")
urdumarks = int(input())
print ("please enter your maths marks:")
mathsmarks =  int(input())
print ("please enter your criminal justice marks:")
CJmarks = int(input())
print ("please enter your islamiat marks:")
Islmarks = int(input())

totalmarks= englishmarks+urdumarks+mathsmarks+CJmarks+Islmarks
percentage = totalmarks/500*100

print ("Total marks: "+str(totalmarks))
print ("Percentage: "+str(percentage)+"%")



