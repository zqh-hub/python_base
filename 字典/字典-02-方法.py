# 1、dict.clear()：清空所有项，就地操作，没有返回值
phone_book = {"coco": "12345", "gogo": "34332"}
phone_book.clear()
print(phone_book)  # {}

# 练习
x = {}
y = x  # 此时，x,y指向同一个字典，id相同
x["key"] = "value"
x = {}  # 此时，x指向了另一个字典，与y的id不同
print(x)  # {}
print(y)  # {'key': 'value'}

a = {}
b = a
a["key"] = "value"
a.clear()
print(a)  # {}
print(b)  # {}  a 和 b 一直指向同一个字典

# 2、copy()
x = {"username": "coco", "happy": ["games", "movies"]}
y = x.copy()
y["username"] = "gogo"
y["happy"].remove("movies")
print(y)  # {'username': 'gogo', 'happy': ['games']}
print(x)  # {'username': 'coco', 'happy': ['games']}

# 扩展
from copy import deepcopy

x = {"username": "coco", "happy": ["games", "movies"]}
y = deepcopy(x)
y["username"] = "gogo"
y["happy"].remove("movies")
print(y)  # {'username': 'gogo', 'happy': ['games']}
print(x)  # {'username': 'coco', 'happy': ['games', 'movies']}

# 3、dict.get(key,[default])：访问指定key的值，key不存在返回None,可指定默认值
u = x.get("username")
u = x.get("ds", "gogo")  # gogo
print(u)

# 4、dict.items()：返回搜索键值对
# keys()\value()
items = x.items()
print(items)

# 5、dict.pop(key)：删除指定的key，并将key的value返回
value = x.pop("username")
print(x)  # {'happy': ['games', 'movies']}
print(value)  # coco

# 6、popitem()：随机删除某个key-value,并返回被删除的key-value
popitem = y.popitem()
print(popitem)
print(y)

# 7、dict.setdefault(key,value)：没有key，就新增key；有key，就获取key的值
phone_book = {"coco": "12345", "gogo": "34332"}
phone_book.setdefault("age", "12")
kv = phone_book.setdefault("coco", "0000")
print(phone_book)  # {'coco': '12345', 'gogo': '34332', 'age': '12'}
print(kv)  # 12345

# 8、dict.update()：字典合并，有相同的项就更新，不同的就添加
people = {"name": "coco", "age": 23}
add = {"age": 90, "height": 173}
people.update(add)
print(people)  # {'name': 'coco', 'age': 90, 'height': 173}
