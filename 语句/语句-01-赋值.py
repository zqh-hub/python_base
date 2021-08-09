# 一、在谈print
# 1、指定分隔符
print("hello", "python", sep="_")  # hello_python
# 2、指定结束字符
print("hello", end="\t")
print("python")  # hello	python

# 二、序列解包
# 1、同时赋值多个(序列解包)
x, y, z = 1, 2, 3
print(x, y, z)

# 2、交换值
x = 1
y = 2
x, y = y, x
print(x, y)  # 2 1

# 左右个数不等时
x, y, *z = 1, 2, 3, 4, 5
print(x, y, z)  # 1 2 [3, 4, 5]

x, *z, y = 1, 2, 3, 4, 5
print(x, y, z)  # 1 5 [2, 3, 4]

# 三、链式赋值
x = y = 1
# 等价于
a = 1
b = a

# 四、增强赋值
x += 1
y *= 2
