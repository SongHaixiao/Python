'''
06. 有一个数列，其前三项分别为1、2、3，
从第四项开始，每项均为其相邻的前三项之和的1/2，
问：该数列从第几项开始，其数值超过1200，试编程实现。
'''

n1 = 1
n2 = 2
n3 = 3

count = 3
sum = 0

while sum <= 1200:
    sum = (n1 + n2 + n3) / 2
    n1 = n2
    n2 = n3
    n3 = sum
    count = count+1

print("From the %dth, the value is over 1200" % (count))