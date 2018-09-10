
'''
# 数组可变类型
n1 = [11,22,33,44,55]
n2 = n1
n3 = n1[:]

n1[-1] = 66
n3[-1] = 99

print("n1",n1)
print("n2",n2)
print("n3",n3)
'''

'''
# 函数默认参数

def fun(arg, list=[]):
    list.append(arg)
    return list

v1 = fun(1)
v2 = fun(2, [])
v3 = fun(3)

print("v1", v1)
print("v2", v2)
print("v3", v3)

'''


'''
# 多态继承
class Base:
    def __init__(self):
        print('Base.init')

class Right(Base):
    def __init__(self):
        print('Right.init')
        Base.__init__(self)

    def r_fun(self):
        print('Right!!!')
        self.l_fun()

    def l_fun(self):
        print('Right_left!!!')

class Left:
    def l_fun(self):
        print('Left!!!')

class Child(Left, Right):
    pass

obj = Child() # init
obj.r_fun()
'''
