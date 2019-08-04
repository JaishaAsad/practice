a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
def add(num1 , num2):
    my_sum = num1 + num2
    print(my_sum)
add(a,b)

#for subtraction
a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
def sub(num1 , num2):
    my_sub = num1 - num2
    print(my_sub)
sub(a,b)

#for multiplication
a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
def mul(num1 , num2):
    my_mul = num1 * num2
    print(my_mul)
mul(a,b)

# # num=int (input("enter the number:"))
# # def even_or_odd (num):
# #     if num  % 2 == 0:
# #         result ="It is an even number"
# #     else:
# #         result="It is an odd number"
# #     return result
# # output_of_function= even_or_odd (num)
# # print(output_of_function)

# a=2
# def my_func():
#     a = 9
#     print(a)

# my_func()
# print(a)

#INNER FUNCTION
def calculate_taxes(percent):
    def actual_tax(salary):
        return salary * percent
    return actual_tax

actual_tax_fn = calculate_taxes(0.88)
print(actual_tax_fn)
print(actual_tax_fn(100000))