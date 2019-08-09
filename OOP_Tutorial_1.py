#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:47:28 2019

@author: ChihChi
"""


class Employee:
    
    num_of_empls = 0
    raise_amount = 1.04
    
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_empls += 1
        
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):    
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        
        first,last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
import datetime

my_date = datetime.date(2019, 8, 18)
print(Employee.is_workday(my_date))
    

print(dir(Employee))

emp_1 = Employee('Charlie', 'Kuo', 90000)
emp_2 = Employee('Ivy', 'Kuo', 80000)

Employee.set_raise_amount(1.05)
    

emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_empls)









