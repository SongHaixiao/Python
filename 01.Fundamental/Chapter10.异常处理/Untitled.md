# 异常概述

[toc]

## 什么是异常

- 异常即是一个事件，该事件会在程序执行过程中发生，影响程序的正常执行。异常发生之后，异常之后的代码就不执行了。

- 异常事件在Python中是一个对象，表示一个错误。当Python脚本发生异常时需要捕获处理它，否则程序会终止执行。

## 什么是异常处理

Python解释器检测到错误，触发异常（也允许程序员自己触发异常），程序员编写特定的代码，专门用来捕捉这个异常（这段代码与程序逻辑无关，与异常处理有关），如果捕捉成功则进入另外一个处理分支，执行为其定制的逻辑，使程序不会崩溃，这就是异常处理。

## 为什么要进行异常处理

Python解析器去执行程序，检测到一个错误时，触发异常，异常触发后且没被处理的情况下，程序就在当前异常处终止，后面的代码不会运行。

所以必须提供一种异常处理机制，以此来增强程序的健壮性与容错性。

## 标准异常

- 常见异常

<img src="C:/Users/xxnzj/Documents/GitHub/Python/01.Fundamental/Chapter10.异常处理/Resources/01.jpg" style="zoom:80%;" />

- 其他异常

<img src="C:/Users/xxnzj/Documents/GitHub/Python/01.Fundamental/Chapter10.异常处理/Resources/02.jpg" style="zoom:80%;" />

<img src="C:/Users/xxnzj/Documents/GitHub/Python/01.Fundamental/Chapter10.异常处理/Resources/03.jpg" style="zoom:80%;" />



# 异常处理

异常是由程序的错误引起的，语法上的错误跟异常处理无关，必须在程序运行前进行修正。

## if 判断方式处理异常

```python
num = input('输入一个字符串试试 >>: ')		# 输入一个字符串试试
if num.isdigit():
    int(num)	# 正确程序，其余的都是异常处理
    print("输入的是 数字字符串，正确")
elif num.isspace():
    print('若输入的是空格，就执行此代码')
elif len(num)==0:
    print('若输入的是空，就执行此代码')
else:
    print("其他情况，执行次代码")
```

### 缺点

if 是可以解决异常的，只是存在以上两个问题：

1. if判断式的异常处理只能针对某一段代码，对于不同的代码段的相同类型的错误需要写重复的if来进行处理。
2. 在实际的程序中频繁地写与程序本身无关而与异常处理有关的if，会使得代码可读性降低。

```python
def test():
    print("test running")

choice_dic={
    '1':test
}

while True:
    choice=input('>>: ').strip()
    if not choice or choice not in choice_dic: continue # 异常处理机制的一种
    choice_dic[choice_dic]()
```

# 基本语法



## try 捕获语法

```python
# format
try:
    code	# 运行别的代码
except<name>:
    code	# 如果在 try 部分引发了异常
except<name>,<data>:
    code	# 如果引发了异常，获得附加的数据
else:
    code 	# "try 内代码块没有异常则执行 else 代码"
finally:
    code 	# 无论异常与否，都会执行该模块，通常是进行清理工作
    
```

### try 的工作原理

当开始一个 try 语句后， Python 就在当前程序的上下文中做标记，这样当异常出现时就可以回到这里，try 字句先执行，接下来会发生什么依赖于执行时是否出现异常。

如果当try后的语句执行时发生异常，Python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。

如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。

如果在try子句执行时没有发生异常，Python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

### 例子

- 打开一个文件，在该文件中的写入内容

```python
try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！！")
except IOError:
    print("Error: 没有找到文件或 读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
```

```python
# Output

内容写入文件成功
```

## 总结

try…except这种异常处理机制就是取代if，让程序在不牺牲可读性的前提下增强健壮性和容错性。

异常处理中为每一个异常定制了异常类型（Python中统一了类与类型，类型即类），对于同一种异常，一个except就可以捕捉到，可以同时处理多段代码的异常（无须写多个if判断式），减少了代码，增强了可读性。

# Python 常见标准异常



Python为每一种异常定制了一个类型，然后提供了一种特定的语法结构用来进行异常处理.

## 1. 处理 ZeroDivisionError

ZeroDivisionError : 除数为 0 的异常，这是一个数学常识，如果在数学运行中没有考虑这样一个因素就有可能引发这一样一个异常。

```python
try:
    print(5/0)
except ZeroDivisionError:   # 'ZeroDivisionError' 除数等于 0 的报错方式
    print("You can't divide by zero!")
```

- 例子：

```python
print("Enter two numbers.")
print("Enter 'q' to quit.")

while True:

    first_number = input("\nfirst_number: ")
    if first_number == 'q':
        break
    second_number = input("second_number: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:	# 依赖于 try ... 执行成功的放入 e
        print('result = {0}'.format(result))
```

- output

```txt
Enter two numbers.
Enter 'q' to quit.

first_number: 2
second_number: 3
result = 0.6666666666666666

first_number: 4
second_number: 0
You can't divide by 0.

first_number: q

```



## 2. 使用异常避免崩溃

发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。

这种情况经常会出现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)
```

- Output

```txt
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First Number: 3
Second Number: 4
0.75

First Number: 2
Second Number: 0
Traceback (most recent call last):
  File "C:/Users/xxnzj/Documents/Files/Code/Python/Quize.py", line 10, in <module>
    answer = int(first_number)/int(second_number)
ZeroDivisionError: division by zero
```



这个程序没有采取任何处理错误的措施，因此让它执行除数为0的除法运算时，它将崩溃.

程序崩溃会给用户带来操作不友好的负面效果。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。

例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。

通过将可能引发错误的代码放在try…except代码块中，可提高这个程序抵御错误的能力。错误是执行除法运算的代码行导致的，因此需要将它放到try…except代码块中。这个实例还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中。

```python
print("Enter two numbers.")
print("Enter 'q' to quit.")

while True:

    first_number = input("\nfirst_number: ")
    if first_number == 'q':
        break
    second_number = input("second_number: ")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

- Output

```txt
Enter two numbers.
Enter 'q' to quit.

first_number: 3
second_number: 4
0.75

first_number: 0
second_number: 0
You can't divide by 0!

first_number: q
```

让Python尝试执行try代码块中的除法运算，这个代码块只包含可能导致错误的代码。依赖于try代码块成功执行的代码都放在else代码块中。

在这个实例中，如果除法运算成功，就使用else代码块来打印结果。

**except代码块告诉Python，出现ZeroDivisionError异常时该怎么办**。如果try代码块因除零错误而失败，就打印一条友好的消息，告诉用户如何避免这种错误。程序将继续运行，用户根本看不到traceback。

## 3.处理 FileNotFoundError

文件为空异常，在操作文件中经常遇到。

```python
filename = 'tom.txt'        # tom 这个文件是不存在的
try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:   # 文件不能找到的异常处理
    print("Sorry! The file " + filename + " can't find.")
else:   # 依赖于 try ... 执行成功的放入 e
    pass
```

- 例子 （一）：

```python
filename = 'old man and sea.txt'  # 这里的文件是存在
try:
    with open(filename, 'rb') as file:  # 注意: 这里的阅读模式要用 'rb' 以二进制的形式读取
        contents = file.read()
except FileNotFoundError:
    print("Sorry! We don't find " + filename + ".")
else:
    # 计算文件大概有多少单词
    words = contents.split()  # 按空格拆分单词
    num_words = len(words)
    print("The file " + file + " has about " + str(num_words) + " words.")

```

- 读取失败

```txt
Sorry! We don't find old man and sea.txt.
```

- 读取成功

```txt
The file old man and sea.txt has about 8 words.
```

- 例子 （二）：使用函数的方式

  ```python
  def count_words(filename):
      try:
          with open(filename, 'rb') as file:
              contents = file.read()
      except FileNotFoundError:
          print("Sorry! We don't find " + filename + ".")
      else:
          # 计算文件大概有多少单词
          words = contents.split()    # 按空格拆分单词
          num_words = len(words)
          print("The file " + filename + " has about " + str(num_words) + " words.")
  
  count_words("Security Introduce.txt")
  count_words("Old Man and Sea.txt")
  
  ```

  

  

- 输出

  ```python
  Sorry! We don't find Security Introduce.txt.
  The file Old Man and Sea.txt has about 8 words.
  ```

  

### 4. 万能异常 Exception

万能异常 Exception，即**可以捕获任意异常**

```python
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print(e)
else:   # 依赖于 try 成功执行引入 e
```

- 输出

```txt
invalid literal for int() with base 10: 'hello'
```

#### 万能异常 Exception 的讨论

1. 如果想要的效果是，无论出现什么异常，统一丢弃或者使用同一段代码逻辑去处理，这时只有一个Exception就足够了。

   ```python
   s1 = 'hello'
   try:
       int(s1)
   except Exception as e:
       # 丢弃或者执行其他逻辑
       print(e)
   ```

   

​		如果统一用Exception，没错，是可以捕捉所有异常，但意味着你在处理所有异常时都使用同		

​		一个逻辑去处理（这里说的逻辑即当前expect下面跟的代码块）。

2. 如果想要的效果是，对于不同的异常需要定制不同的处理逻辑，那就需要用到多分支了。

- 多分支处理：

  ```python
  s1 = 'hello'
  try:
      int(s1)
  except IndexError as e:
      print(e)
  except KeyError as e:
      print(e)
  except ValueError as e:
      print(e)
  ```

  

- 多分支 + Exception

  ```python
  s1 = 'hello'
  try:
      int(s1)
  except IndexError as e:
      print(e)
  except KeyError as e:
      print(e)
  except ValueError as e:
      print(e)
  except Exception as e:
      print(e)
  ```

- 其他形式的异常

  ```python
  s1 = 'hello'
  try:
      int(s1)
  except IndexError as e:
      print(e)
  except KeyError as e:
      print(e)
  except ValueError as e:
      print(e)
  # except Exception as e:
  #     print(e)
  else:
      print("try 内代码块没有异常则执行 else 代码")
  finally:
      print("无论异常与否，都会执行该模块，通常是进行清理工作")
  ```

  

### 5. 自定义异常

python 异常分为两种：

- 内建异常，即Python自己定义的异常
- 用户自定义异常，即自定义异常扩展了异常机制

<img src="C:/Users/xxnzj/Documents/GitHub/Python/01.Fundamental/Chapter10.异常处理/Resources/04.jpg" style="zoom:80%;" />

可以看到Python的异常有个大基类，然后继承的是Exception。所以自定义类也必须继承Exception。

- 自定义异常类的语法格式

  ```python
  # 最简单的自定义异常
  class FError(Exception):
      pass
  ```

- 抛出异常用 try...except:

  ```python
  try:
      raise FError("自定义异常")
  except FError as e:
      print(e)
  ```

  

- 一个简单的自定义异常类模板

  ```python
  class CustomError(Exception):
      def __init__(self,ErrorInfo):
          super().__init__(self)  # 初始化父类
          self.errorinfo = ErrorInfo
  
      def __str__(self):
          return self.errorinfo
  
  if __name__ == '__main__':
      try:
          raise CustomError("客户异常")
      except CustomError as e:
          print(e)
  ```

  

# 手动抛出异常



## raise 手动抛出异常

当程序出错时，Python会自动触发异常，也可以通过raise显式引发异常，一旦执行了raise语句，raise之后的语句将不再执行。

如果加入了try…except，那么except里的语句会被执行。

- raise 语法格式如下：

  ```python
  raise [Exception [, args [, tracback]]]
  ```

  - 语句中Exception是异常的类型（例如NameError）
  - args是一个异常参数值,该参数是可选的，如果不提供，异常的参数是None。
  - 最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。

一个异常可以是一个字符串、类或对象。

Python的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。

- 定义一个异常：

  ```python
  def functionName( level ):
      if level < 1:
          raise Exception("Invalid level!", level)
          # 触发异常后，后面的代码就不再执行
  ```

  **注意：为了能够捕获异常，except语句必须用相同的异常来抛出类对象或者字符串。**

- 捕获以上异常，except 语句如下：

  ```python
  try:
      # 正常逻辑
      pass
  except "invalid level!":
      # 触发自定义异常
      pass
  else:
      # 其余代码
      pass
  ```

  **注意：手动抛出的异常如果不捕获，同样会中断程序运行。**

- raiise 捕获手动抛出的异常：

  ```python
  def testRaise():
      for i in range(5):
          try:
              if i == 2:
                  raise NameError
                  # print('hello')
          except NameError:
              print("Raise a NameError!")
          print(i)
      print('end.....')
  
  testRaise()
  ```

  - 输出

  ```txt
  0
  1
  Raise a NameError!
  2
  3
  4
  end.....
  ```

  

- assert 捕获抛出异常

  ```python
  def testRaise():
      for i in range(5):
          try:
              assert i < 2 # 当 i < 2 不成立时，就会抛出异常
          except AssertionError:
              print("Raise a AssertionError!")
          print(i)
      print('end.....')
  
  testRaise()
  ```

  

- 输出

  ```txt
  0
  1
  Raise a AssertionError!
  2
  Raise a AssertionError!
  3
  Raise a AssertionError!
  4
  end.....
  ```

  

- 自定义一个异常并抛出自定义异常

  ```python
  class RangeError(Exception):
      def __init__(self,value):
          self.value = value  # value 是异常发生时的信息
  
      def __str__(self):          # 返回异常发生时的信息的字符串
          return self.value
  
  def testRaise():
      for i in range(5):
          try:
              if i == 2:
                  raise RangeError("RangeError")
          except RangeError as e:
              print(e)
          print(i)
      print('end.....')
  
  testRaise()
  ```

  - 输出

  ```txt
  0
  1
  RangeError
  2
  3
  4
  end.....
  ```

  ## assert 语句

  使用assert是学习Python一个非常好的习惯，Python的assert语句格式及用法很简单。

  **在没完善一个程序之前，开发者不知道程序在哪里会出错，与其让它在运行时崩溃，不如在出现错误条件时就崩溃，这时候就需要assert的帮助。**

- 定义

  - **assert是声明其布尔值必须为真的判定，如果发生异常就说明表达式为假。可以理解assert语句为raise…if…not，用来测试表达式，其返回值为假，就会触发异常。**
  - **assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好地知道是哪里出了问题。**

- 语法格式

  ```python
  assert expression [, arguments]
  assert expression [, parameters]
  ```

- 例子

  ```python
  assert 1 == 1
  assert 2 + 2 == 2 * 2
  assert len(['my boy', 12]) < 10
  assert range(4) == [0,1,2,3]
  assert len(lists) >= 5, '列表元素小于 5'
  assert 2 == 1, '2 不等于 1'
  ```