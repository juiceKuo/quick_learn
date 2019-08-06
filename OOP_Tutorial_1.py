#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:47:28 2019

@author: ChihChi
"""


class Employee:
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    
        
emp_1 = Employee('Charlie', 'Kuo', 90000)
emp_2 = Employee('Ivy', 'Kuo', 80000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
