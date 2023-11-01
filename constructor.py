# class employee:
#     def__init__(self,name,age,salary):
#         self.name= name 
#         self.age=age
#         self.salary=salary
#     def employee_details(self):
#         print("name of employee:",self.name)
#         print("age of employee:",self.age)
#         print("salary of employee:",self.salary)
# E1=employee("abhi","19","10000")
# E1.show()


class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID:%d\nName:%s"%(self.id,self.name))
emp1= Employee("ram",101)
emp2= Employee("shyam",102)
emp1.display()
emp2.display()


class parent_class:   
    def print2(self):
        print("parent class function")

class child_class(parent_class):
    def print1(self):
        print("child class function")
obj=child_class()
obj.print2()
obj.print1() 