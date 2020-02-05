# _*_ coding utf-8 _*_
# 开发时间：2020/2/322:17
# 开发人员：Administrator
# 文件名称：循环
# score = 75
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# --------------------------------------------
# for i in range(1,15,2):
#     print(i)
# -----------------------------------
# n=1
# while n< 10:
#     print(n)
#     n = n+1
# else:
#     print("循环结束")
# -----------------------------------
# for i in range(1,10):
#     for j in range(1,i+1):
#
#         print(f'{i} * {j} = {i*j}',end= " ")
#     print()
# -----------------------------------
# i=1
# while i <9:
#     j=1
#     while j<=i:
#         print(f'{i} * {j} = {i*j}',end= " ")
#         j+=1
#     i+=1
#     print()
# -----------------------------------
# while True:
#     s = input("输入0退出：")
#     if s =='0':
#         break
#     print("你输入的是：",s)
# -----------------------------------
# for s in 'python':
#     if s == 'y':
#         continue
#     print(s)
# -----------------------------------
# import random
# target = random.randint(1,100)
# total = 5
# count =0
# while True:
#     n = int(input("请输入猜的数字0-100："))
#     if n > target:
#         print("大了")
#     elif n< target:
#         print("小了")
#     else:
#         print("猜对了")
#         break
#     count +=1
#     if count >= total:
#         print("游戏结束，猜了",total,'次了')
#         print(f"游戏结束，猜了{total}次了")

# -----------------------------------
