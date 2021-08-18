# raise Exception([message])
""" 常见异常
    Exception   几乎所有的异常类都是从它派生而来的
    AttributeError  引用属性或给它赋值失败时引发
    OSError     操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
    IndexError  使用序列中不存在的索引时引发，为LookupError的子类
    KeyError    使用映射中不存在的键时引发，为LookupError的子类
    NameError   找不到名称（变量）时引发
    SyntaxError     代码不正确时引发
    TypeError   将内置操作或函数用于类型不正确的对象时引发
    ValueError   将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
    ZeroDivisionError   在除法或求模运算的第二个参数为零时引发
"""


# 自定义异常
class SelfException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):  # 这里就是异常的字符串信息
        return self.message


# raise SelfException("哈哈")

# 捕捉异常
def add():
    a = 1
    b = 0
    try:
        res = a / b
    except Exception:
        print("错了")


add()

""" 所有的异常都会捕捉到
    try:
        xxx
    expect:
        xxx
"""

""" 捕捉多个异常
    try:
        xxx
    exception (YYYY,ZZZ) as e:
        xxx
"""
"""
    try:
        xxx
    except:
        xxx
    else:   出现异常时，不会走else
        xxx
"""
try:
    print(1 / 1)
except:
    print("异常")
else:
    print("else")

"""
    try:
        xxx
    expect:
        xxx
    finally:   有没有异常都会执行finally
        xxx
"""
try:
    print(1 / 0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")


# 异常的好处。下面两个函数的效果一样，但是test_02效率更好，test_01函数查找了两次(lst[0])
def test_01():
    lst = ["coco"]
    if lst[0]:
        print(lst[0])
    else:
        print("没有")


def test_02():
    lst = ["coco"]
    try:
        print(lst[0])
    except:
        print("没有")
