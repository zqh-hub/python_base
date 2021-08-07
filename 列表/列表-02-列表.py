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

# ---------------------------------- 列表方式 ----------------------------------
# 1、append(obj):追加到列表末尾
lst = [1, 2, 3]
lst.append(4)
print("lst---------", lst)

# 2、clear(): 清空列表;与lst[:] = []类似
lst.clear()
print("lst---------", lst)

# 3、copy():复制列表
a = [1, 2, 3]
b = a
print(id(a), id(b))  # id一样

c = a.copy()  # 类似：a[:]或list(a)
print(id(a), id(c))  # id不一样

# 4、lst.count(org):计算org在lst中出现的次数
res = [1, 2, 3, 1, 2, 3, 4, 3, 3, 5].count(3)
print(res)

res = [[1, 2], [3, 4], [1, 2]].count([1, 2])
print(res)

# 5、lst1.extend(lst2):将lst2扩展到lst1中
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
# 注意，extend与 + 是有区别的：a+b是返回新值，extend是直接修改a
c = [1, 2, 3]
d = [4, 5, 6]
cd = c + d
print(cd)  # [1, 2, 3, 4, 5, 6]
# 注意，extend与 append 是有区别的：append直接视为整体
e = [1, 2, 3]
f = [4, 5, 6]
e.append(f)
print(e)  # [1, 2, 3, [4, 5, 6]]

# 使用切片实现extend
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)  # [1, 2, 3, 4, 5, 6]

# 6、lst.index(org):获取org在lst中第一次出现的索引;找不到报错
a = ["coco", "jojo", "coco"]
i = a.index("coco")
print(i)

# 7、lst.insert(index,org):将org插入到lst的index位置
a = ["coco", "jojo", "coco"]
a.insert(2, "gogo")
# a.index(5, "jojo")   超过范围，报错TypeError: slice indices must be integers or have an __index__ method
print(a)
# 通过切片实现insert
a = ["coco", "jojo", "coco"]
a[2:2] = ["gogo"]
print(a)
