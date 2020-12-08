

from Mnogochlen import *
from PartOfMnogochlen import *
def main():
    termsforfirst, termsforsecond, done = [],[], True
    numberofpmchf = int(input('Введите количество членов первого многочлена: '))

    while done:
        print('\nВыберите действие')
        print('\nДля умножения многочленов нажмите 1')
        print('\nДля возведения многочлена в степень нажмите 2')
        p = input()
        if p == '1':
            numberofpmchs = int(input('Введите количество членов второго многочлена: '))
            coefficient, power = input('\nВведите коэффициент здесь: '), input('Введите степень здесь: ')
            if coefficient.isalpha() or power.isalpha():
                raise TypeError('Введены некорректные данные')
            elif numberofpmchf != 0:
                print('Первый многочлен выглядит так: ', end= ' ')
                termsforfirst.append(PartOfMnogochlen(int(coefficient), int(power)))
                showme(termsforfirst)
                numberofpmchf-=1
            elif numberofpmchs != 0:
                print('Второй многочлен выглядит так: ', end= ' ')
                termsforsecond.append(PartOfMnogochlen(int(coefficient), int(power)))
                showme(termsforsecond)
                numberofpmchs -= 1
                if numberofpmchs == 0:
                    print('\nСпасибо за использование программы')
                    done  =  False
                    f, s = Mnogochlen(termsforfirst), Mnogochlen(termsforsecond)
                    Mnogochlen.__mul__(f, s)
        if p == '2':
            coefficient, power = input('\nВведите коэффициент здесь: '), input('Введите степень здесь: ')
            if coefficient.isalpha() or power.isalpha():
                raise TypeError('Введены некорректные данные')
            elif numberofpmchf != 0:
                print('Первый многочлен выглядит так: ', end=' ')
                termsforfirst.append(PartOfMnogochlen(int(coefficient), int(power)))
                showme(termsforfirst)
                numberofpmchf -= 1
                if numberofpmchf == 0:
                    print('\nСпасибо за использование программы')
                    done  =  False
                    print ('\nВведите степень, в которую хотите возвести многочлен')
                    n = input()
                    n = int(n)
                    s = Mnogochlen(termsforfirst)
                    Mnogochlen.fastExp(s,n)
def showme(listofpmch):
    for pmch in listofpmch:
        if pmch.get_power() == 0:
            x = ""
        else:
            x = "x"
        if pmch.get_coefficient() >= 1:
            plus = "+"
        else:
            plus = "-"
        print('{0}{1}{2}^{3} '.format(plus, pmch.get_coefficient(), x, pmch.get_power()), end=' ')
main()