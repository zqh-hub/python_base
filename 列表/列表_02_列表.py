# list(): 可将任何序列（而不仅仅是字符串）作为list的参数
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']
# ''.join(list):将字符列表转化为字符串
print("".join(['h', 'e', 'l', 'l', 'o']))  # hello

# 赋值
x = [1, 2, 1]
# 修改
x[1] = 1
print(x)
# 删除元素
y = [3, 4, 5]
del y[2]
print(y)

# 切片赋值
name = list("hello")
name[0:3] = "ggggg"
print(name)
# 切片插入新值
n = [1, 2, 3]
n[1:1] = [5, 6, 7]  # [1, 5, 6, 7, 2, 3]
print(n)

# 切片删除值
a = [1, 2, 3, 4]
a[1:3] = []
print(a)  # [1, 4]

# 步长
b = [1, 2, 3, 4, 5, 6, 7, 8]
b[2:5:2] = [0, 0]
print(b)
