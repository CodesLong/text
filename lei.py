# _*_ coding utf-8 _*_
# 开发时间：2020/2/421:29
# 开发人员：Administrator
# 文件名称：lei
class Person:
    def __init__(self,name,sex,birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday
    def say(self,word):
        print(f'{self.name}说："{word}"')
zhangsan = Person('张三','男','23232323')
zhangsan.say('你好')
lisi = Person('历史','nu','23232323')
lisi.say('nihao')