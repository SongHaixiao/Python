'''
    03.某百货公司为了促销，采用购物打折的办法。
    消费满1000元以上者，按九五折优惠；
    2000元以上者，按九折优惠；
    3000元以上者，按八五折优惠；
    5000元以上者，按八折优惠。
    编写程序，输入购物款数，计算并输出优惠价。
'''

money = float(input("Input money : "));

if money >= 0 and money < 1000:
    print("no sale, final money is ", money)
elif money >= 1000 and money < 2000:
    print("95% on sale, final money is ", money * 0.95)
elif money >= 2000 and money < 3000:
    print("90% on sale, final money is ", money * 0.90)
elif money >= 3000 and money < 5000:
    print("85% on sale, final money is ", money * 0.85)
elif money >= 5000:
    print("80% on sale, final money is ", money * 0.80)
else:
    print("Money inputed is illegal")