s = "hello,python"
# 1、center(宽度,填充):居中
ss = s.center(20, "*")
print(ss)  # ****hello,python****

# 2、ljust(宽度,填充)：左对齐。rjust():右对齐
ss = s.ljust(20, "*")
print(ss)

# 3、str.find(org,[start,end]): 返回org在str中的第一次出现的下标，没有返回-1。从左面开始查找
index = s.find("o")
print(index)

index = s.find("o", 5)  # 指定下标，搜索范围
print(index)
# 4、rfind()： 从右面开始查找
r_index = s.rfind("o", 0, -1)
print(r_index)

# 5、str.index(org,[start,end]) 也是返回org在str出现的下标。与find()不同的是，如果org不存在会报错
i = s.index("o", 1, 9)
print(i)  # 4
i = s.rindex("o")
print(i)  # 10

# 6、str.count(org,[start,end]): 返回org在str中出现的次数
res = s.count("o")
print(res)  # 2

# 7、str.join(seq):将str与seq的每个元素进行拼接，seq的元素必须是字符串
lst = ["1", "2", "3"]
res = '+'.join(lst)
print(res)  # 1+2+3

# 8、lower() upper()
# 扩展：islower、istitle、isupper、translate。
res = s.upper()
print(res)
s = res.lower()
print(s)
print(s.islower())  # True

# 9、str.replace(old,new): 将old替换为new
res = s.replace("o", "G")
print(res)  # hellG,pythGn

# 10、str.split(org): 以org为分隔符，分割str。如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）处进行拆分
res = s.split(",")
print(res)  # ['hello', 'python']

# 11、str.strip([org]): 返回str两边删除org后的字符串,不指定org，默认是空格
s = "*hello*world*"
res = s.strip("*")
print(res)  # hello*world
# 扩展：lstri()p、rstrip():只删除一边
res = s.lstrip("*")
print(res)

# str.translate(table)
s = "hello,python"
# str.maketrans(old, new, dele) # dele指要删除哪些字符
table = s.maketrans("ho", "HO", ",")  # 首先制作转化对照表
res = s.translate(table)  # 然后进行替换
print(res)  # HellOpytHOn
