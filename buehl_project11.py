#!python3
#buehl_project10.py - Advanced scripting/ OOP

import sys, os

class Employee:
    def __init__(self, empID, first, last, telNum, rmNum):
        self.empID = empID
        self.first = first
        self.last = last
        self.telNum = telNum
        self.rmNum = rmNum

    def getName(self):
        return(self.first + ' ' + self.last)

    def getDirString(self):
        return '{}: {}, {}, {}, {}'.format(self.empID, self.last, self.first, self.telNum, self.rmNum)

class salEmployee(Employee):
    def __init__(self, empID, first, last, telNum, rmNum, sal):
        super().__init__(empID, first, last, telNum, rmNum)
        self.sal = sal

    def DirString(self):
        return Employee.getDirString(self).ljust(44) + '| $' + self.sal


class hrlyEmployee(Employee):
    def __init__(self, empID, first, last, telNum, rmNum, hrsWorked, hrlyRate):
        super().__init__(empID, first, last, telNum, rmNum)
        self.hrsWorked = hrsWorked
        self.hrlyRate = hrlyRate

    def changeHrs(self):
        hrs = input('Hours Worked: ')
        if hrs in quitters:
            sys.exit()
        self.hrsWorked = hrs
    
    def DirString(self):
        owed = (float(self.hrsWorked) * float(self.hrlyRate))
        #return '{}: {}, {}, {}, {} | ${}'.format(self.empID, self.last, self.first, self.telNum, self.rmNum, owed)

        return Employee.getDirString(self).ljust(44) + '| $' + str(owed)


# Employee Database
emp_1 = salEmployee('1', 'Jacob', 'Dirk', '+1(513)292-7375', '421', '3600')
emp_2 = hrlyEmployee('2', 'Duncan', 'McDonald', '+1(513)444-8314', '201', 0, '9.50')
emp_3 = salEmployee('3', 'Sizzle', 'Geirhart', '+1(216)952-1650', '002', '3300')
emp_4 = salEmployee('4', 'Colin', 'Spaulding', '+1(800)669-8909', '003', '1100')
emp_5 = hrlyEmployee('5', 'Christian', 'Matthew', '+1(444)555-8888', '202', 0, '15.00')

employees = [emp_1, emp_2, emp_3, emp_4, emp_5]



# main program 
quitters = ['x', 'quit', 'exit', 'clear']
while True:

 #print Employee list
    print('x to quit\n')
    print('Employees:')
    for emp in employees:
        print(emp.DirString())
    print()

#select Employee to edit
    #input checking
    while True:
        empSelector = input('Update Hours for Employee(empID): ')
        if empSelector in quitters:
            sys.exit()
        try:
            int(empSelector)
            while True:
                if int(empSelector) in range(len(employees)+1):
                    break
                else:
                    empSelector = input('Enter Legitimate Employee ID: ')
                    if empSelector in quitters:
                        sys.exit()
            break
        except ValueError:
            print('Not a Number')


    for emp in employees:
        if empSelector == emp.empID:
            chEmployee = emp
        else:
            continue

    try:
        chEmployee.changeHrs()
    except AttributeError:
        print(chEmployee.getName() + ' is a salary Employee')
        input()

    os.system('clear')