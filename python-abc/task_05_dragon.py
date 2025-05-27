#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        self.swim = True
    print("The creature swims!")


class FlyMixin:
    def fly(self):
        self.fly = True
    print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        self.roar = True
    print("The dragon roars!")

    def draco(self):
        Dragon.fly()
        Dragon.swim()
        Dragon.roar()
