# Fibonacci 1 1 2 3 5 8 13 21 ..

first = 1
second = 1
print(first)
print(second)

# third =  first + second
# fourth = second + third  : almost impossible to apply to very large Numbers.

# for i in [0,1,2,3,4,5,6,7,8,9] :
for i in range(10) :
    oldFirst = first
    first = second
    second = oldFirst + second
    print(second)

# Another method using list : saved for later

# fiboList = [1, 1]
#
# for i in range(10) :
#



# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
# print (fibonacci(9))
