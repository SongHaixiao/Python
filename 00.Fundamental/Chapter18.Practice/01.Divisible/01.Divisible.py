'''
    01.输入一个整数n，判断其能否同时被5和7整除，
    如能，则输出“××能同时被5和7整除”；否则输出“××不能同时被5和7整除”。
    要求“××”为输入的具体数据。
'''

integer_number = int(input("Input an integer : "))

if(integer_number % 5 == 0) and (integer_number % 7 == 0):
    print(integer_number, "can be divisible 5 and 7 at the same time.")

else:
    print(integer_number, "can't be divisible 5 and 7 at the same time.")