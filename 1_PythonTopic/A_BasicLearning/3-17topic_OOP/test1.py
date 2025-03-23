# @Version  :1.0
# @Author   :李祎凡
# @File     :test1
# @Time     :2025/3/17 上午11:07
# @Other    :文件说明


class Employee:
    __name = None
    __salary = None
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_annual(self):
        return self.__salary*12

class Worker(Employee):
    def __init__(self, name, salary):
        super().__init__(name,salary)
    def work(self):
        print(f"{self.__name}员工工作")



class Manager(Employee):
    bonus = None
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def manage(self):
        print(f"{self.__name}经理管理")

    def get_annual(self):
        return (self.__salary*12 + self.bonus)

def show_emp_annual(emp:Employee):
    print("该员工年薪为:",emp.get_annual())

def working(emp:Employee):
    if isinstance(emp, Manager):
        Manager.manage(emp)
    elif isinstance(emp, Worker):
        Worker.work(emp)

manage = Manager("lyf",10000,5000)
work = Worker("kss",6000)

show_emp_annual(manage)
show_emp_annual(work)

working(manage)
working(work)









