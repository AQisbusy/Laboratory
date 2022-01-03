class Student(object):
    def __init__(self,name,tel):
        self.name = name
        self.tel = tel
    def print_tel(self):
        print('%s:%s'%(self.name,self.tel))


big = Student('Bigben',65290)
Ji = Student('Jim',62741)

A = big.print_tel()
B = Ji.print_tel()



String = 'I have %d friends.'

refine = '%s'%(String)

print(refine)
