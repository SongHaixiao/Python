'''
Question :
    05.编程求解“百马百瓦问题”：
    有100匹马驮100块瓦，大马驮3块，
    中马驮2块，两个小马驮1块。
    问大马、中马、小马各有多少匹？
'''

# formula 1 : 3x + 2y + 0.5z = 100
# formula 2 : x + y + z = 100
# then new formula : 5x + 3y = 100

for x in range(0, 100):
    for y in range(0, 100):
        if 5*x + 3*y == 100:
            z = 100 - x - y
            print("Big horse %d, Middle horse %d, Little horse %d" % (x, y, z))