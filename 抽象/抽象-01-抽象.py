# 斐波那契
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

# callable()
'''
callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
'''


# 针对函数
def add():
    "这里是注释文档"
    print("hello")


print(add.__doc__)  # 这里是注释文档

print(callable(add))  # True


# 针对方法
class People:
    def say(self):
        print("python")


p = People()
print(callable(p.say))  # True

# 针对类
print(callable(People))  # True

# 针对未实现__call__方法的实例对象
print(callable(p))  # False


# # 针对实现了__call__方法的实例对象
class B:
    def __call__(self, *args, **kwargs):
        return 0


b = B()
print(callable(b))  # True

# 函数外与函数内的变量赋值影响
# 当函数里的变量是字符等不可变类型时，局部变量复制为新值时，那么局部变量与外边的变量已经不再有联系，分别指向不同的值
s = "python"
def str_change(ss):
    ss = "java"
print(s)

# 类型于：
s = "python"
ss = s
ss = "java"
print(s)

# 当函数里的变量是列表等可变类型时，局部变量仅仅时进行修改里面的元素操作，不会改变这两个变量的指向
def change(n):
    n[0] = "2"

ns = ["1", "2"]
change(ns)
print(ns)

# 类似于：
ns = ["1", "2"]
nn = ns
nn[0] = "2"
print(ns)

# 为了解决可变类型出现的这种情况
ns = ["1", "2"]
nn = ns[:]  # ns与nn是相等(==)但不同(is)的列表


def change(n):
    n[0] = "2"
change(nn)
print(ns)  # 没有影响
