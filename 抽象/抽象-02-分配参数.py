# 分配参数
def add(x, y):
    print(x + y)


# par = (1, 2)
# par = [1, 2]
par = 1, 2

add(*par)

par = {"name": "coco", "age": 12}


def hello(name, age):
    print(name, age)


hello(**par)
