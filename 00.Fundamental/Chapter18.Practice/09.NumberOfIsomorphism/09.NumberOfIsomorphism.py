'''
09.编写程序找出1与100之间的全部“同构数”。
“同构数”是这样一种数，它出现在它的平方数的右端。
例如，5的平方是25，5是25中右端的数，5就是同构数，
25也是一个同构数，它的平方是625。
'''

def IsomorphismNumber(num):
    n = num * num;
    digit4 = n % 1000;
    digit3 = n % 100;
    digit2 = n % 10;

    if num == digit4 or num == digit3 or num == digit2 :
        print(num , " is a isomorphism number")
    else:
        print(num , " is not a isomorphism number")

num = int(input("Input a integer number from 1 to 100 : "))

IsomorphismNumber(num)
