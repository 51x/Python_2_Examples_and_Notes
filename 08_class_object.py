#!/usr/bin/python
# -*- coding: utf-8 -*-

class Calculator:
    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a*self.b

newCalculation = Calculator(22,44)

print 'a+b: %d'%newCalculation.add()

print 'a*b: %d'%newCalculation.mul()


class Scientific(Calculator) :
    def power(self):
        return pow(self.a, self.b)


newPower = Scientific(6,7)
print 'a+b: %d'%newPower.add()
print 'a*b: %d'%newPower.mul()
