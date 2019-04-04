#!python3
# buehl_project9.py - Advanced scripting/ OOP

class Employee:
    
    def __init__(self, first, last, telNum, rmNum):
        self.first = first
        self.last = last
        self.telNum = telNum
        self.rmNum = rmNum
    
    def DirString(self):
        return '{}, {} - {} - {}'.format(self.last, self.first, self.rmNum, self.telNum)

emp_1 = Employee('Jacob', 'Dirk', '+1(513)292-7375', '1+(216)789-7663')
emp_2 = Employee('Duncan', 'McDonald', '+1(513)444-8314', '1+(937)205-7396')
emp_3 = Employee('Sizzle', 'Geirhart', '+1(216)952-1650', '1+(122)124-9990')

empList = [emp_1.DirString(), emp_2.DirString(), emp_3.DirString()]

print('\nEmployee List:\n')
for emp in empList:
    print(emp)

print('\ndone.')