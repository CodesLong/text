# _*_ coding utf-8 _*_
# 开发时间：2020/2/421:41
# 开发人员：Administrator
# 文件名称：guanli_xitong
student_data = [

    {
        'id':12,
        'name':'a',
        'sex':'nan',
        'address':'sjfie'

    },
    {
        'id':121,
        'name':'a44',
        'sex':'nan',
        'address':'sj79+fie'

    },
    {
        'id': 122,
        'name': 'a11',
        'sex': 'nan',
        'address': 'sjfi467e'

    },


]
# 美化显示f
def beauty(student_data):
    for student in student_data:
        print(student)
# 1, 显示
def showAll():
    for student in student_data:
        print(student)
# 2, 新建
def creatStudent():
    name = input('输入名字：')
    sex = input('输入性别：')
    address = input('输入地址：')
    student = {
        'name':name,
        'sex':sex,
        'address':address
    }
    student_data.append(student)
# 3, 查询
def findStudent():
    name = input('查询名字：')
    for student in student_data:
        if student['name'] ==name:
            print(student)
            return
        else:
            print('查找失败')

# 4, 修改
def modify_student():
    name = input('查询名字：')
    for student in student_data:
        if student['name'] ==name:
            print(student)
            student['name'] = input('输入名字：')
            student['sex'] = input('输入性别：')
            student['address'] = input('输入地址：')
    else:
        print('查找失败')
# 5, 删除
def remove_student():
    name = input('查询名字：')
    for student in student_data:
        if student['name'] ==name:
            print(student)
            student_data.remove(student)
    else:
        print('查找失败')
while True:
    print("""
    0.退出
    1,显示
    2,新建
    3,查询
    4,修改
    5,删除
    """)
    operation = input('请输入数字序号：')
    if operation =='1':
        showAll()
        print('显示所有信息，待完善')
    elif operation == '2':
        creatStudent()
        print('新建信息')
    elif operation =='3':
        findStudent()
        # print('查询信息')
    elif operation =="4":
        modify_student()
        # print('修改信息')
    elif operation =='5':
        remove_student()
        # print('删除信息')
    elif operation =='0':
        print('退出系统')
        break