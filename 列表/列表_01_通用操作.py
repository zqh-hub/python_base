# 序列：列表、元组、字符串
# 容器：序列、映射（如:字典）
# 通用序列操作：索引、切片、相加、相乘、成员资格

# 索引
print("hello"[0])
print("hello"[-1])
# res = input("year:")[3]
# print(res)

# 切片
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[9:-21])
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[7: 10])
print(nums[-3:])
print(nums[:])
print(nums[::-1])

# 序列相加
print([1, 2] + [3, 4])
print("hello" + " world")

# 乘法
print("python  " * 5)
print([None] * 4)

# 成员资格
print("h" in "hello")
ls = [
    ["coco", "1234"],
    ["jojo", "3456"]
]
print(["coco", "1234"] in ls)

print(len(ls))
print(max(nums))
print(max(2, 5, 8))
print(min(nums))
