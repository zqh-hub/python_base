# 序列和映射基本上是元素（item）的集合，要实现它们的基本行为（协议），
# 不可变对象需要实现2个方法，而可变对象需要实现4个
a = {"name": "coco", "age": 12}
print(a.__len__())
print(a.__getitem__("name"))
a.__setitem__("gender", "0")  # 仅可变
print(a)
a.__delitem__("gender")  # 仅可变
print(a)


# 函数property
class MyClass:
    def __init__(self):
        self._name = None

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    info = property(get_name, set_name, del_name, "docs")


m = MyClass()
m.info = "coco"  # 自动调用set_name
print(m.info)  # 自动调用get_name

del m.info  # 自动调用del_name


# __getattribute__
class MyCls:
    def __init__(self, name):
        self.name = name

    def my_def(self):
        print("vvvvvvvvvv")

    def __getattribute__(self, item):
        print("开始属性校验拦截功能")
        print(item)
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return "没有"


c = MyCls("jojo")
print("---------------", c.name)  # 在获取属性(方法)时，会将 name的值作为实参传递给item，然后__getattribute__方法做一系列的操作，最后返回值


# __getattr__
class MyCls:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("没有属性时，调用我")
        return None

    def __setattr__(self, key, value):
        print("赋值调用我")

    def __delattr__(self, item):
        print("删除时调用")


c = MyCls("jojo")
c.age  # 没有该属性，就会调用__getattr__
c.age = 12  # 调用__setattr__
del c.age  # 调用__delattr__
