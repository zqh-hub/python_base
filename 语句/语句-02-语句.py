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
