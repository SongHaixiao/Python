'''
    02. 输入一个百分制的成绩，
    经判断后输出该成绩的对应等级。
    其中，90分以上为“A”，
    80～89分为“B”，
    70～79分为“C”，
    60～69分为“D”，
    60分以下为“E”。
'''
score = int(input("Input a score (0 ~ 100) : "))

if score >= 90 and score <= 100:
    print(score, " is A ")
elif score >= 80 and score <= 89:
    print(score, " is B ")
elif score >= 70 and score <= 79:
    print(score, " is C ")
elif score >= 60 and score <= 69:
    print(score, " is D ")
elif score >= 0 and score <= 59:
    print(score, " is E ")
else:
    print("Score inputed is illegal")