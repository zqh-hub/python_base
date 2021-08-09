# 创建,键是唯一的
phone_book = {"coco": "12345", "gogo": "34332"}
res = dict([("name", "gogo"), ("age", "12")])
print(res)  # {'name': 'gogo', 'age': '12'}
res = dict(name="coco", age=32)
print(res)  # {'name': 'coco', 'age': 32}

# 取值
name = res["name"]
print(name)  # coco

# 长度
l = len(res)
print(l)  # 2

# 成员资格，key in dict
print("name" in res)  # True

# 删除
del res["name"]  # {'age': 32}
print(res)
del res

# 键的类型：可以是任何不可变数据类型(如：字符串、元组)
# 自动添加：没有key,赋值后就有了


# format_map():格式化功能用于字典
phones = {"coco": "12345", "gogo": "34332"}
print("coco的号码是：{coco}".format_map(phones))  # coco的号码是：12345
