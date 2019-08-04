# name = "Jaisha"
# print ("hello "+name)
# print ("i m best")
# print ("i m student of criminology")
# name = "QASIM"
# print ("hello "+name)
# print ("i m best")
# print ("i m student of criminology")

# def printData(name):
#   print("Hello "+name+" from a function")
#   print("Hello this is second line")
#   print ("And this on is third")

# printData("Jaisha")
# printData("Kommal")

# def calculateArea (num):
#  return num*20

# input = 10
# output = calculateArea(input)
# print (output)

# r= int (input ())
# a=3.13*r*r
# c=2*3.13*r
# ans=a+c
# print(ans)

def calcSum(r):
    a=3.13*r*r
    c=2*3.13*r
    ans=a+c
    return ans  


radius1 = int(input())
radius2 = int(input())

circle1=calcSum(radius1)
circle2=calcSum(radius2)

if circle1>circle2:
    print("circle1 is big")
else:
    print("circle2 is big")







