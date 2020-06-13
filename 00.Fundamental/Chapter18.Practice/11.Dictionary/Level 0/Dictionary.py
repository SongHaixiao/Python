import  random

# 判断是否键入单词
# judge whether to input words
def input_word_continue():
    isContinue = 'y'
    while isContinue == 'y' or isContinue == 'Y':
        input_word(dict_words)
        isContinue = input("Does continue to input words (Y/N) ? ")

# 向字典里键入单词
# input word into dictionary
def input_word(dict_words):
    key_english,value_chinese = input("\nInput a english word with its corresponding chinese meaning : ").split()
    dict_words[key_english] = value_chinese


# 判断是否继续查询单词
# judge whether to look up words
def look_up_word_continue():
    isContinue = 'y'
    while isContinue == 'y' or isContinue == 'Y':
        word = input("Input a word to look up : ")
        look_up_word(word)
        isContinue = input("Does continue to look up words (Y/N) ? ")

# 查询单词
# look up words
def look_up_word(word):
    if dict_words:
        isFind = False
        chinese = ""
        english = ""
        for key, value in dict_words.items():
            if key == word:
                isFind = True
                english = word
                chinese = dict_words[english]
                break
            elif value == word:
                isFind = True
                english = key
                chinese = word
                break
        if isFind:
            print(english +  " : " + chinese)
    else:
        print("This dictionary is empty!")

# 判断是否继续测试单词
# judge whether continue to check words
def check_word_continue():
    isContinue = 'y'
    while isContinue == 'y' or isContinue == 'Y':
        check_word()
        isContinue = input("Does continue to look up words (Y/N) ? ")


# 测试单词
# check words
def check_word():
    if dict_words:
        count = 5
        correct = 0
        guess = list(dict_words.keys())
        while count > 0:
            guess_english = random.choice(guess)
            guess_chinese = dict_words[guess_english]
            user_input = input("\nInput the word \'" + guess_english + "\' corresponding chinese meaning : ")

            if user_input == guess_chinese:
                correct += 1

            count -= 1

        correct_percent = correct / 5 * 100

        print("This test result : %.2f%% correct!" %(correct_percent))

    else:
        print("This dictionary is empty!")

# 判断主测试函数是否继续
# udge whether continue to select option
def select_option_continue():
    isContinue = 'y'
    while isContinue == 'y' or isContinue == 'Y':
        print(
            '''
                  WELCOME TO USE DICTIONARY
                  - Input 1 to insert wrods
                  - Input 2 to look up words
                  - Input 3 to check wrods
            ''')
        select_option()
        isContinue = input("Does continue to use DICTIONARY (Y/N) ? ")

# 选项
# select_option
def select_option():
    option = int(input("Input option : "))
    if option == 1:
        input_word_continue()
    elif option == 2:
        look_up_word_continue()
    elif option == 3:
        check_word_continue()
    else:
        print("Error Input!")



dict_words = {}

select_option_continue()