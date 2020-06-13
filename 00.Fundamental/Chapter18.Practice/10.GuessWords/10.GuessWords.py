###########################
# Word Jumple 猜单词游戏  #
##########################

import random

# Create Words tuple - 创建单词序列元组
WORDS = ("python", "juice", "easy",
         "difficult", "answer", "continue",
         "phone","hello","pose","game")

print(
    """
            欢迎参加猜单词游戏
        把字母组合称一个正确的单词
    """
)
isContinue = 'y'

while isContinue == 'y' or isContinue == 'Y':
    # 从序列中随机挑出一个单词
    word = random.choice(WORDS)

    # 一个用于判断玩家是否猜对的变量
    correct = word

    # 创建乱序后的单词
    jumble = ""
    while word : # word 不是空串循环
        # 根据 word 长度，产生 word 的随机位置
        position = random.randrange(len(word))

        # 将 position 位置字母组合到乱序u后的单词
        jumble += word[position]

        # 通过切片，将 position 位置的字母从原单词中删除
        word = word[:position] + word[(position + 1):]

    print("\n乱序后的单词 : ", jumble)

    guess = input("请你猜: ")

    while guess != correct and guess != "":
        print("对不起, 不正确")
        guess = input("继续猜： ")

    if guess == correct:
            print("真棒， 你猜对了")

    isContinue = input("是否继续（Y/N）: ")