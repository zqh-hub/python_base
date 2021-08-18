class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(self.name)


def fun():
    print("fun")


p1 = Person()
p1.set_name = fun
p1.set_name()

""" 私有方法\私有属性"""


# from xx import yy,无法导入私有方法\私有属性

class Secretive:
    __name = "cc"  # 变成了私有的属性

    def __pri(self):  # 私有的方法
        print("私有的方法")

    def pri(self):
        self.__pri()
        print("还是出来了")


s = Secretive()
s.pri()
print("-" * 20)
# python对私有的幕后处理方式：
# 在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头加上一个下划线和类名：Secretive._Secretive__inaccessible
s._Secretive__pri()  # 访问私有方法

"""关于继承"""


class AA:
    pass


class A(AA):
    def a(self):
        print("a")


class B:
    def b(self):
        print("b")


class a(A, B):
    def a(self):
        print("aa")


# 确定一个类是否是另一个类的子类
res = issubclass(a, A)  # True
# 查看类的基类
res = a.__bases__  # (<class '__main__.A'>, <class '__main__.B'>)
print(res)

# 判断实例对象是否是某个类的实例
aa = a()
res = isinstance(aa, a)
print(res)  # True
# 使用isinstance有局限性，即使不是直接实例对象也会认为是True，在抽象基类的情况下才是最妥当的，见抽象-04
res = isinstance(aa, AA)  # True
print("---", res)


# 对于多重继承中，两个父类都有相同的方法，左面的父类会覆盖右面的（先入为主）
class C:
    name = "coco"

    def read_self(self):
        print("-------------------a")


class D:
    def read_self(self):
        print("-------------------b")


class E(C, D):
    pass


e = E()
e.read_self()  # -------------------a

# hasattr() 判断时候含有属性或方法
print(hasattr(e, "read_self"))  # True
print(hasattr(e, "name"))  # True

# 检查属性是否可调用，具体callable用法请看 抽象-01
res = callable(getattr(e, "read_self", None))  # True
print(res)

# setattr 设置属性
setattr(e, "age", 12)
print(getattr(e, "age", None))
