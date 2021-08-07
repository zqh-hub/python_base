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
# a.insert(5, "jojo")   超过范围，报错TypeError: slice indices must be integers or have an __index__ method
print(a)
# 通过切片实现insert
a = ["coco", "jojo", "coco"]
a[2:2] = ["gogo"]
print(a)

# 8、pop([index]):从列表中删除指定下标的元素，默认删除最后一个，并返回被删除的元素
x = ["jojo", "coco", "gogo"]
res = x.pop()
print(x, res)
y = ["jojo", "coco", "gogo"]
y.pop(1)
print(y)

# 练习，通过append 与 pop实现栈的后进先出
a = [1, 2, 3]
res = a.pop()  # 最后的弹出去
a.append(res)  # 添加到末尾
print(a)

# 9、lst.remove(org)：删除指定元素(第一个出现的)。就地修改且不返回值
a = ["1", "2", "3", "1", "2"]
a.remove("1")
print(a)  # ['2', '3', '1', '2']

# 10、reverse()：相反的顺序。就地修改且不返回值
a = ["1", "2", "3"]
a.reverse()
print(a)
# 拓展：reversed(seq):这个函数不返回列表，而是返回一个迭代器
a = ["1", "2", "3"]
res = list(reversed(a))
print(res)

# 11、lst.sort([reverse]):就地排序,对原列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本
a = [3, 1, 5, 4, 1, 2]
a.sort(reverse=True)  # [1, 1, 2, 3, 4, 5]
a.sort(reverse=True)  # [5, 4, 3, 2, 1, 1]
print(a)

# 为实现排序可返回，可使用sorted(seq,[reverse])
a = [3, 1, 5, 4, 1, 2]
s = sorted(a)  # [1, 1, 2, 3, 4, 5]
r = sorted(a, reverse=True)  # [5, 4, 3, 2, 1, 1]
print(s)
print(r)
