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
