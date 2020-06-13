# 5.2.1.py
# 5.2流程控制语句之条件语句 示例代码一

''' 
运用 input() 输入函数、print() 输出函数、if else 条件语句 
判断所键入的账号、密码是否正确
正确输出 Sucess
错误输出 Fail
'''

'''
Pylint 规范：
1.常量 大写
2.程序末尾需要空出一行
'''

ACCOUNT = 'hello'
PASSWORD = 'world'

print("please input account:")
user_account = input()

print("please input password:")
user_password = input()

if user_account == ACCOUNT and user_password == PASSWORD :
    print("Sucess")
    
else :
    print("Fail")
