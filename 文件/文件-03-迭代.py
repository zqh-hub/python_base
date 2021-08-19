# 一个字符一个字符的
import fileinput

with open("file_03.txt") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        print(char)

# 一行一行的
with open("file_03.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

# 读取所有
with open("file_03.txt", "r") as f:
    for char in f.read():
        print("---------------------------", char)

with open("file_03.txt", "r") as f:
    for line in f.readlines():
        print(line)

print("*" * 30)
# fileinput
for line in fileinput.input("file_03.txt"):
    print("行号", fileinput.lineno())
    print(line)

""" 推荐迭代方式 """
with open("file_03.txt") as f:
    for line in f:
        print(line)
