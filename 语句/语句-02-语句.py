# 三目表达式
res = "True" if True else "False"
print(res)  # "True"

# 比较运算符
"""
x == y
x < y
x > y
x <= y
x >= y
x != y
x is y
x is not y
x in y
x not in y
"""

# 字符串比较大小，按照unicode排序
res = "sas" < "qwq"
print(res)
# ord()：将字符转化为码点
# chr()：将码点转化为字符
print(ord("s"))  # 115
print(ord("q"))  # 113

print(chr(12121))  # ⽙

# 序列的比较
res = [1, 2] < [3, 4]

# 断言：assert 条件,解释

age = 12
assert 1 < age < 11, "age 不在范围内"
print(age)

# 布尔运算符
"""
and
not
or
"""

# enumerate(seq):返回key-value
strings = ["python", "hello"]
for index, s in enumerate(strings):
    if "python" in s:
        strings[index] = "[N]"

print(strings)

# 推导式
res = [x for x in range(10)]
print(res)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 等价于：
res = []
for x in range(10):
    res.append(x)
print(res)

res = [x for x in range(10) if x % 2 == 0]
print(res)  # [0, 2, 4, 6, 8]
# 等价于：
res = []
for x in range(10):
    if x % 2 == 0:
        res.append(x)
print(res)  # [0, 2, 4, 6, 8]

res = [(x, y) for x in range(3) for y in range(3)]
print(res)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 等价：
res = []
for x in range(3):
    for y in range(3):
        res.append((x, y))
print(res)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# exec
exec("print('hello')")

# eval():
res = eval("12")
eval("print('hello')")
print(res)
