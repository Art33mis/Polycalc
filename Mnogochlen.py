from PartOfMnogochlen import *
class Mnogochlen:
    def __init__(self, terms: list):
        self._terms = terms


    # Этот метот умножает два многочлена
    def  __mul__(self, s_poly_obj):
        result = {}
        for f_poly in range(0, self.__len__()):
            for s_poly in range(0, s_poly_obj.__len__()):
                the_new_power = self.get_poly()[f_poly].get_power() + s_poly_obj.get_poly()[s_poly].get_power()
                the_new_coefficient = self.get_poly()[f_poly].get_coefficient()\
                                    * s_poly_obj.get_poly()[s_poly].get_coefficient()

                if the_new_power not in result:
                    result[the_new_power] = the_new_coefficient
                else:
                    result[the_new_power] = result.get(the_new_power) + the_new_coefficient

        result.keys()
        result2 = [0]*(max(result.keys())+1)
        for i, item in result.items():
            result2[i] = item
        return Mnogochlen(result2)

    def __len__(self):
        return self._terms.__len__()



    def get_poly(self):
        if self._terms:
            return self._terms
        else:
            return None

    # Метод выводит многочлен в привычном для нас виде
    def print_poly(self):
        print('This is the answer: ', end=' ')
        for p, c in reversed(list(enumerate(self._terms))):
            if p == 0:
                x = ""
            else:
                x = "x"
            if c >= 1:
                plus = "+"
            else:
                plus = "-"
            print('{0}{1}{2}^{3} '.format(plus, c, x, p), end= ' ')

    def fastExp(self, n):
        if n % 2 == 0:
            s_object = Mnogochlen
            if n == 0:
                return 1
            p = (self * self).fastExp(n // 2)
        if n % 2 != 0:
            if n == 1:
                return self
            p = self*self.fastExp(n - 1)
        p.print_poly()
        return p
