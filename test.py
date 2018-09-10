class Parent(object):

    def __new__(cls, *args, **kwargs):
        print('Parent__new__')
        print(cls)
        return super().__new__(Child)

    def __init__(self,name,age):
        print('Parent__init__')
        self.name = name
        self.age = age

    def say(self):
        print('Parent_say')

    def __enter__(self):
        print('Parent_enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Parent_exit')


class Child(Parent):
    '''
    def __init__(self,name,age):
        print('Child_init')
        self.name = name
        self.age = age

    '''

    def __new__(cls, *args,**kwargs):
        print('Child__new__')
        return super().__new__(cls)


    def __enter__(self):
        print('Child_enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Child_exit')

    def say(self):
        print('Child_say')


with Child('name',12)as obj:
    print(obj)
    print('with')
    print(obj.name,obj)
    print(obj.age,obj)
    obj.say()



from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(20) as exc:

'''
class SignleClass(object):
    __instance = None
    __attr = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self,name,age):
        if not self.__attr:
            self.name = name
            self.age = age
            SignleClass.__attr = True


obj1 = SignleClass('name',2)

obj2 = SignleClass('name2',3)

print(obj1,obj2,obj1.name,obj2.name)
'''



'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%s * %s = %s"%(j,i,i*j),end='  ')
    print()
'''

