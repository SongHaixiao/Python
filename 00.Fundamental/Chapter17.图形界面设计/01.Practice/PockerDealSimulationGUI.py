from tkinter import *
import random

n = 52          # 假设包含 52 张牌，不包括大王和小王

# gen_pocker(n) 函数实现对 n 张牌进行洗牌。
# 方法是随即产生两个下标，将此下标的列表元素交换，以达到洗牌目的.
# 列表元素存储的是某张牌（实际上是牌的编号).
def gen_pocker(n):
    x=100
    while(x>0):
        x=x-1
        p1=random.randint(0,n-1)
        p2=random.randint(0,n-1)
        t=pocker[p1]
        pocker[p1]=pocker[p2]
        pocker[p2]=t
    return pocker

# main function

# 将要发的 52 张牌， 按梅花 0 ~ 12， 方块 13 ~ 25， 红桃 26 ~ 28，黑桃 39 ~ 51
# 顺序编号并存储在 pocker 列表（未洗牌之前）.
pocker=[i for i in range(n)]

# 调用 gen_pocker(n) 函数实现对 n 张牌的洗牌
pocker = gen_pocker(n)  # 实现对 n 张牌的洗牌
print(pocker)
(player1,player2,player3,player4)=([],[],[],[])    # 四位牌手各自手中牌的图片列表
(p1,p2,p3,p4)=([],[],[],[])                        # 四位牌手各自手中牌的编号列表

# 创建一个 Canvas,设置其背景色为白色
root=Tk()
cv = Canvas(root, bg='white', width=700, height=600)

# 将要发的 52 张牌的图片，按梅花 0 ~ 12，
# 方块 13 ~ 25, 红桃 26 ~ 38, 黑桃 39 ~ 51 的顺序编号，
# 存储到扑克牌图片 imgs 列表中。
# 也就是说，imgs[0] 存储梅花 A 的图片 "1-1.gif"， imgs[1] 存储梅花 2 的图片 "1-2.gif",
# imgs[14] 存储方块2的图片 "2-2.gif", 依次类推。
# 目的是让程序可以根据牌的编号找到对应的图片
imgs=[]
for i in range(1,5):
    for j in range(1,14):
        imgs.insert((i-1)*13+(j-1), PhotoImage(file=str(i)+'-'+str(j)+'.gif'))

# 实现每轮发四张牌，每位牌手发一张，总计 13 发牌，每位牌手最终各有 13 张牌
for x in range(13):     # 13 轮发牌
    m=x*4
    p1.append(pocker[m])
    p2.append(pocker[m+1])
    p3.append(pocker[m+2])
    p4.append(pocker[m+3])

# 牌手对牌进行排序，就相当于理牌，使同花色的牌连在一起
p1.sort()
p2.sort()
p3.sort()
p4.sort()

# 根据每位牌手手中牌的编号绘制对应的图片进行显示
for x in range(0, 13):
    img = imgs[p1[x]]
    player1.append(cv.create_image((200+20*x, 80), image=img))
    img = imgs[p2[x]]
    player2.append(cv.create_image((100,150+20*x), image=img))
    img = imgs[p3[x]]
    player3.append(cv.create_image((200+20*x, 500), image=img))
    img = imgs[p4[x]]
    player4.append(cv.create_image((560,150+20*x), image=img))

print("player1:",player1)
print("player2:",player2)
print("player3:",player3)
print("player4:",player4)
cv.pack()
root.mainloop()
