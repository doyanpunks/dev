import pytest

class Employee:
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, default_raise=5000):
        self.annual_salary += default_raise 

"""    def give_raise(self, salary_raise=0):
            if salary_raise == 0:
                default_raise = 5000
                self.annual_salary += default_raise
            else:
                self.annual_salary += salary_raise
"""
