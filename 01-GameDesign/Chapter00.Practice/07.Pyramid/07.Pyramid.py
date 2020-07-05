'''
8. 编写一个函数，调用该函数能够打印一个由指定字符组成的n行金字塔。
其中，指定打印的字符和行数n分别由两个形参表示。
'''

def Pyramid(c, n):
    for x in range(0,n):

        for y in range(0, n - x):
            print(" ", end='')

        for z in range(0,x + 1):
            print("%c" %(c), end=' ')

        print()

c = input("Input one character : ")
n = int(input("Input one number : "))

Pyramid(c,n)
