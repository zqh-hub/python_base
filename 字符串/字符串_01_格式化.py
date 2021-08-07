# 百分号格式化
s = "hello,%s! hello,%s!" % ("world", "python")
print(s)  # hello,world! hello,python!

# format
# 1、匿名
s = "hello,{}! hello,{}!".format("python", "world")
print(s)

# 2、指定键
s = "hello,{x}! hello,{y}!".format(y="python", x="world")
print(s)

# 3、值是序列
lst = ["python", "world"]
s = "hello,{lst[0]}! hello,{lst[1]}!".format(lst=lst)
print(s)

# 4、转换类型
s = "{num:x}是十六进制,{num:f}是小数".format(num=122332)
print(s)  # 14是十六进制,12.000000是小数
# 常用的类型
'''
b 将整数表示为二进制数
c 将整数解读为Unicode码点
d 将整数视为十进制数进行处理，这是整数默认使用的说明符
e 使用科学表示法来表示小数（用e来表示指数）
E 与e相同，但使用E来表示指数
f 将小数表示为定点数
F 与f相同，但对于特殊值（nan和inf），使用大写表示
g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
G 与g相同，但使用大写来表示指数和特殊值
n 与g相同，但插入随区域而异的数字分隔符
o 将整数表示为八进制数
s 保持字符串的格式不变，这是默认用于字符串的说明符
x 将整数表示为十六进制数并使用小写字母
X 与x相同，但使用大写字母
% 将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）
'''
# 5、宽度
s = "{num:5}".format(num=3)
print(s)  # ssss3；s是空格，右对齐
s = "{name:5}".format(name="c")
print(s)  # cssss;s是空格，左对齐
# 6、精度
s = "{num:.3f}".format(num=12.32353)
print(s)  # 12.324  注意：会进位
s = "{:.3}".format("hello")  # 字符串指定精度
print(s)  # hel

# 同时指定宽度和精度
s = "{num:10.3f}".format(num=12.32353)
print(s)  # ssss12.324

# 7、千分位
s = "{:,}".format(10 ** 10)
print(s)  # 10,000,000,000

# 注意：逗号应放在宽度和表示精度的句点之间  {:宽度,精度和类型}
s = "{:20,.3f}".format(10 ** 10)
print(s)  # 10,000,000,000.000

# 8、对齐方式(<:左；>:右；^:居中)
s = "{:<10.2f}".format(12.221212)
print(s)  # 12.22sssss

# 9、填充
s = "{:s<10.2f}".format(12.221212)
print(s)  # 12.22sssss

