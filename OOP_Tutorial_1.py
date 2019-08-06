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
        
    
        
emp_1 = Employee('Charlie', 'Kuo', 90000)
emp_2 = Employee('Ivy', 'Kuo', 80000)

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









