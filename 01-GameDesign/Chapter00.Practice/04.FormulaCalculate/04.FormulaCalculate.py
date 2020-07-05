'''
    04.编写程序，计算下列公式中s的值（n是运行程序时输入的一个正整数）。
    s =1 +（1 + 2）+（1 + 2 + 3）+ … +（1 + 2 + 3 + …+ n）
    s =12+ 22 + 32 + … +（10×n+2）
    s =1×2-2×3+3×4-4×5+ … +（-1）^（n-1）× n x（n+1）
'''

num = int(input("Input a positive integer : "))
s1 = 0
s2 = 0
s3 = 0

for n in range(1,num + 1):
    s1 = s1 + n         # first formula
    s2 = s2 + (10 * n + 2)     # second formula
    s3 = s3 + ((-1) ** (n - 1) * n * (n +1))

print("First formula = ",s1)
print("First formula = ",s2)
print("First formula = ",s3)
