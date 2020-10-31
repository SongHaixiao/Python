# Cards Module
class Card():
    """ A playing card."""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # 牌面数字 1 ~ 13
    SUITS = ['梅', '方', '红', '黑']        # 梅 - 梅花, 方 - 方块, 红 - 红桃, 黑 - 黑桃

    def __init__(self, rank, suit,face_up = True):
        self.rank = rank            # 牌面数字 1 ~ 13
        self.suit = suit            # 花色
        self.is_face_up = face_up   #  是否显示牌正面， True 为 正面， False 为 背面

    # def __str__(self):              # 重写 print() 方法, 打印一张牌的信息
    #     if self.is_face_up:
    #         rep = self.suit + self.rank
    #     else:
    #         rep = "XX"
    #     return  rep

    def pic_order(self):        # 牌的序号
        if self.rank == 'A':
            FaceNum = 1
        elif self.rank == 'J':
            FaceNum = 11
        elif self.rank == 'Q':
            FaceNum = 12
        elif self.rank == 'K':
            FaceNum = 13
        else:
            FaceNum = int(self.rank)

        if self.suit == '梅':
            Suit = 1
        elif self.suit == '方':
            Suit = 2
        elif self.suit == '红':
            Suit = 3
        else:
            Suit = 4

        return (Suit - 1) * 13 + FaceNum

# Hand 类
class Hand():
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []     # cards 列表变量存储牌手的牌

    # def __str__(self):      # 重写 print() 方法，打印出牌手的所有牌
    #     if self.cards:
    #         rep = ""
    #         for card in self.cards:
    #             rep += str(card) + "\t"
    #     else:
    #         rep = "无牌"
    #     return rep

    def clear(self):          # 清空手里的牌
        self.cards = []

    def add(self, card):      # 增加牌
        self.cards.append(card)

    def give(self, card, other_hand):   # 把一张牌给别的牌手
        self.cards.remove(card)
        other_hand.add(card)

    def print(self):                # 用 属性 打印 所有的牌
        for card in self.cards:
            print(card.suit + card.rank, end=" ")

# Poke 类
class Poke(Hand):
    """ A deck of playing cards. """
    def populate(self):             # 生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):              # 洗牌
        import random
        random.shuffle(self.cards)  # 打乱发牌的顺序

    def deal(self, hands, per_hand = 13):   # 发牌, 默认发给每个牌手 13 张牌
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card, hand) # 上两句，可以用此句替换
                else:
                    print("不能继续发牌了, 牌已经发完了！")
# 主程序
if __name__ == "__main__":
    print("============= This is a module with classes for playing cards ==========")

    # 4 players
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    poke1.populate()        # 生成一副牌
    poke1.shuffle()         # 洗牌
    poke1.deal(players, 13) # 发给每个牌手 13 张牌

    # 显示 4 players 的牌

    # 通过 __str__ 类 解 类 输出
    # n = 1
    # for hand in players:
    #     print("牌手", n, end = ":")
    #     hand.print()
    #     n = n + 1

    # 调用 类 属性输出
    n = 1
    for hand in players:
        print("牌手", n, end = ":")
        hand.print()
        print()
        n = n + 1
    input("\nPress the enter key to exit.")