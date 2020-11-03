import math


class Collisions:
    count = 0

    def __init__(self, m1, m2, v1, v2):
        self.m1 = m1
        self.m2 = m2
        self.v1 = v1
        self.v2 = v2

    def calculate(self):
        count = 0
        const = 0.5*self.m1*(self.v1)**2 + 0.5*self.m2*(self.v2)**2
        speed1 = (((self.m1-self.m2)*self.v1)/(self.m2+self.m1))
        speed2 = ((2*self.m1*self.v1)/(self.m1+self.m2))

        self.count += 2
        self.v1 = speed1
        self.v2 = speed2
        print(self.v1, self.v2, self.count)

        if speed1 > speed2:
            self.count += 1
            return self.count


if __name__ == "__main__":
    col = Collisions(100000, 1, 10, 0)
    for i in range(10):
        col.calculate()
