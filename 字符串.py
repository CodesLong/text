# _*_ coding utf-8 _*_
# 开发时间：2020/2/416:50
# 开发人员：Administrator
# 文件名称：字符串
# s = "床前明月光"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[-1])
# print(s[1:4:2])   # 切片 步长
# print(s[:3])
# print(s[:])
# -------------------------
# a = "你"
# b = 'he'
# print('{}对{}说："hello"'.format(a,b))
# print(f'{a}对{b}说："hello"')  # f-string 表达方式，省去format
# # 用 + 来连接不同的字符串
# print('are '+" you "+"ok")
# -------------------------
# 列表
# a = [1,2,'ad',1.2]
# print(a[1])
# a.append(111)
# print(a)
# a.insert(1,'aaa') # 插入指定位置
# print(a)
# a.extend("sss")
# print(a)
# a.pop(0)
# print(a)
# a.remove('ad')
# print(a)
# a[1] = 000
# print(a)
# 元组 ()----------------------------------
# a = (1,2,'ad',1.2)
# print(a)
# print(a[1:3])
# ---------------------------------
# 字典{ key：value}
# a = {'aa':'12',
#      'age':"123"
#      }
# print(a)
# a["age"] = 222
# print(a)
# a['fav'] = "打篮球"
# print(a)
# -------------------------------
a = 1
s = 0
while a<=100:
    s+=a
    a+=1
print(s)
def he(a,m):
    """
    :param a: 起始数
    :param m: 终止数
    :return: 结果
    """
    b = 0
    while a<=m:
        b += a
        a += 1
    return b
print(he(5,100))