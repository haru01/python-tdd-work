

from functional import seq

result1 = seq(1, 2, 3, 4) \
    .map(lambda x: x * 2) \
    .filter(lambda x: x > 4) \
    .reduce(lambda x, y: x + y)

print(result1)


result3 = 0
for i in seq(1, 2, 3, 4):
    tmp1 = i * 2
    if (tmp1 > 4):
        result3 += tmp1
print(result3)

class NomalPointCalc():
    def calc_point(self, base):
        return base

class SilverPointCalc():
    def calc_point(self, base):
        return base * 1.5

class GoldPointCalc():
    def calc_point(self, base):
        return base * 3


class XxxContext():
    def __init__(self):
        self.__point_calcs = {}
        self.__point_calcs['Nomal']  = NomalPointCalc()
        self.__point_calcs['Silver'] = SilverPointCalc()
        self.__point_calcs['Gold']   = GoldPointCalc()

    def calc(self, type, point):
        return self.__point_calcs[type].calc_point(point)


print(XxxContext().calc('Nomal', 100))
print(XxxContext().calc('Silver', 100))
print(XxxContext().calc('Gold', 100))