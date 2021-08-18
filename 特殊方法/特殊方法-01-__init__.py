"""
    __init__ 构造函数
"""


# 情况1：子类没有重写__init__,子类的实例直接获取父类的属性
class A:
    def __init__(self):
        self.name = "coco"

    def get_name(self):
        print(self.name)


class B(A):
    def get_age(self):
        print("12")


b = B()
b.get_name()


# 情况2：子类重写了__init__，并且没有关联父类的__init__，报错
class A:
    def __init__(self):
        self.name = "coco"

    def get_name(self):
        print(self.name)


class B(A):
    def __init__(self):
        self.age = 12

    def get_age(self):
        print(self.age)


# b = B()
# b.get_name()


# 继承父类的构造函数的方法
class A:
    def __init__(self):
        self.name = "coco"

    def get_name(self):
        print(self.name)


class B(A):
    def __init__(self):
        A.__init__(self)  # 第一种方法,针对旧版python
        self.age = 12

    def get_age(self):
        print(self.age)


b = B()
b.get_name()


class A:
    def __init__(self):
        self.name = "coco"

    def get_name(self):
        print(self.name)


class B(A):
    def __init__(self):
        super().__init__()  # super()
        self.age = 12

    def get_age(self):
        print(self.age)


b = B()
b.get_name()
