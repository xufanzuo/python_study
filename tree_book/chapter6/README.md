# Chapter6 参数
参数(argument or parameter)
python通过赋值进行传递的机制与C++的引用参数选项并不完全相同，但是在实际中，它与c语言的参数传递模型相当相似。
* **不可变参数“通过值”进行传递**。整数，字符串这样的对象是通过 **对象引用**而不是拷贝进行传递，但是你无论怎样都不能在原处改变不可变对象，实际的效果就很像创建了一份拷贝。
* **可变对象是通过“指针”进行传递的**。例如，列表和字典这样的对象也是通过对象引用进行传递的，这一点与C语言使用指针传递数组很相似：可变对象能够在函数内部进行原处的改变，和c数组很像。

### 参数和共享引用
例子：
```python
def f(a)：
    a = 99
b=88
f(b)
print(b)
#88
```
这里的数字，元组为不可改变对象，因此无影响。
```python
def change(a,b):
    a = 2
    b[0] = 'spam'
X=1
L=[1,2]
change(X,L)
#X,L -> (1,['spam',2])
```
这里chang的第二条赋值语句并没有修改b，我们修改的是b当前所引用的对象的一部分。
```python
X=1
a=X
a=2
print(X)
#1

L = [1,2]
b = L
b[0]  = 'spam'
print(L)
#['spam',2]
```

### 避免可变参数的修改
对于可变参数的原处修改的行为不是一个BUG--他只是参数传递在python中的工作方式，在pyhton中，默认通过引用(也就是**指针**)进行函数的参数传递，这通常是我们想要的：*意味着不需要创建多个拷贝就可以在我们程序中传递很大的对象。*
如果不想如此，可以简单的创建一个可变对象的拷贝，
> L = [1,2]
> change(X, L[:])
> def change(a,b)
>   a = b[:]
这个仅仅是防止这些改变会影响调用者，为了真正意义上防止这些改变，可以将 **可变对象** 转换为 **不可变对象**。但是很少使用。
> change(X,tuple(L))

### 特定的参数匹配模型
* **位置**：从左到右
    匹配顺序为从左到右

* **关键字参数**：通过参数名进行匹配
    调用者可以定义哪一个函数接收这个值，通过在调用时使用参数的变量名，使用 *name=value*这种语法

* **默认参数**：为没有传入值的参数定义参数值
    如果调用时传入的值过于少的话，函数能够为参数定义接受的默认值，再一次使用语法 *name=value*

* **可变参数**：收集任意多基于位置或关键字的参数
    函数能够使用特定的参数，它们是以字符 \* 开头，收集任意多的额外参数(这个特性常常叫做 **可变参数**)
* **可变参数解包**： 传递任意多的基于位置或关键字的参数
    调用者能够再使用 \* 语法去将参数集合打散，分成参数。这个 \* 与在函数头部的 * 恰恰相反：在函数头部意味着收集任意多的参数，而在调用者中意味着传递任意多的参数。
* **Keyword-only参数**：参数必须按照名称传递
    在python3.0中(不包括2.6)函数也可以指定参数，参数**必须**用带有关键参数的名字(而不是位置)来传递。这样的参数通常用来定义实际参数以外的配置选项。

python参数匹配步骤：
1. 通过位置分配非关键字参数
2. 通过匹配变量名分配关键字参数
3. 其他额外的非关键字参数分配到*name元组中
4. 其他额外的关键字参数分配到**name字典中
5. 用默认值分配给在头部未得到分配的参数
在这之后，确认每个参数只传入了一个值，否者发生错误。

#### 关键字参数和默认参数的实例
```python
#位置
def f(a,b,c):print(a,b,c)

#关键字
f(c=3,b=2,a=1)

#默认参数
def f(a,b=2,c=3):print(a,b,c)

#关键字和默认参数
def func(spam,eggs,toast=0,ham=0):
    print((spam,eggs,toast,ham))
func(1,2)   # Output: (1,2,0,0)
func(1,ham=1,eggs=0)  # Output: (1,0,0,1)
func(spam=1,eggs=0)  # Output: (1,0,0,0)
func(toast=1,eggs=0,spam=3)  # Output: (3,0,1,0)
func(1,2,3,4)    # Output: (1,2,3,4)

#任意参数的实例
#第一种，*参数 在元组中收集不匹配的位置参数
def f(*args):print(args)
f() #Output: ()
f(1)    #Output: (1,)
f(1,2,3,4)  #Output: (1,2,3,4)

#任意参数的实例
#第二种，**参数 在字典中收集
def f(**args): print(args)
f() #Output: {}
f(a=1,b=2) #Output: {'a':1,'b':2}

#任意参数的实例
#第三种，函数头部混合一般参数，*参数以及 **参数去实现
def f(a,*pargs,**kargs):print(a,pargs,kargs)
f(1,2,3,x=1,y=2) #Output: 1 (2, 3) {'x': 1, 'y': 2}
```

#### 解包参数实例
在调用函数的时候能够使用*语法，在这种情况下，它与函数定义的意思相反。**它会解包参数的集合**，而不是创建参数的集合。例如，我们通过一个元组给一个函数传递四个参数。
```python
def func(a,b,c,d):print(a,b,c,d)

#元组 元组用一个 * 号
args = (1,2)
args +=(3,4)
func(*args) #Output: 1 2 3 4

#字典 字典用两个 * 号
args={'a':1,'b':2,'c':3}
args['d'] = 4
func(**args) #Output: 1 2 3 4

#此外，在调用中能够以非常灵活的方式混合普通的参数，基于位置的参数以及关键字参数
func(*(1,2),**{'d':4,'c':4}) # 1 2 4 4 
func(1,*(2,3),**{'d':4}) # 1 2 3 4  
func(1,*(2,3),d=4) # 1 2 3 4 
```
#### min调用实例
假设编写一个函数，这个函数能够计算任意参数集合和任意对象数据类型集合中的最小值。这个函数应该能够接受零个或多个参数，能够使用所有的Python对象类型。
```python
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first  = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

ef minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
def lessthan(x,y): return x < y  #See also: lambda
def grtrthan(x,y): return x > y

print(minmax(lessthan,4,2,1,5,6,3)) #Self-test code
print(minmax(grtrthan,4,2,1,5,6,3))

```
#### 一个更有用的例子：通用set函数
```python
def intersect(*args):
    res = []
    print(args)
    for x in args[0]:
        print('x:',x)
        for other in args[1:]:
            print('other:',other)
            if x not in other: pass
            else :
                res.append(x)
                print('res:',res)
    return print(res)

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return print(res)

s1, s2, s3 = 'SPAMH', 'SCAM', 'SLAMH'
intersect(s1,s2,s3)
union(s1,s2)

```

