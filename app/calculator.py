import math
import random

class Calculator:
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2

    def plus(self):
        return self.argument1 + self.argument2

    def minus(self):
        return self.argument1 - self.argument2

    def multiplication(self):
        return self.argument1 * self.argument2

    def division(self):
        if self.argument2 != 0:
            return self.argument1 / self.argument2
        else:
            return

    def power(self):
        return math.pow(self.argument1, self.argument2)

    def art(self):
        return (self.argument1 + self.argument2) * random.randint(1,10)
