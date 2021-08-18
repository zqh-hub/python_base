from abc import ABC, abstractmethod


class A(ABC):  # 抽象类不能被实现，只能被继承
    @abstractmethod
    def read(self):
        pass


class a(A):
    def read(self):  # 抽象基类中的抽象方法必须实现
        print("a")


# 在这种情况下，使用isinstance()最妥当
aa = a()
res = isinstance(aa, a)  # True
print(res)

res = isinstance(aa, A)  # True
print(res)


