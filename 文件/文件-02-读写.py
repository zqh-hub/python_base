""" 读取写入逐个字符"""
f = open("file_01.txt", "w")
f.write("hello")
f.close()

s = open("file_01.txt", "r")
txt = s.read(3)  # read([num]):指定读取几个字符,不指定num会读取全部
s.close()
print(txt)

""" 读取写入字符行"""
s = open("file_02.txt", "r")
txt = s.readline()  # readline([num]):也可指定num读取几个字符
s.close()
print(txt)

s = open("file_02.txt", "r")
txt = s.readlines()  # 读取所有，并返回列表
s.close()
print(txt)

s = open("file_02.txt", "w")
s.writelines(["coco\n", "jojo\n", "gogo"])  # 读取所有，并返回列表
s.close()

""" with """
with open("file_02.txt", "w") as f:
    f.writelines(["python\n", "jenkins\n", "linux"])
