'''
09. 编写一个判断完数的函数。
完数是指一个数恰好等于它的真因子（除自身以外的约数）之和，
如6=1+2+3，6就是完数。
'''

def perfect_number(num):
    fractor_sum = 0
    for f in range(1, num):
        if num % f == 0:
            fractor_sum = fractor_sum + f
    if fractor_sum == num:
        print("%d is a perfect number." %(num))
    else:
        print("%d is not a perfect number." %(num))


num = int(input("Input a integer number : "))

perfect_number(num)