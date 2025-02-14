# BMI. Вес/рост*2.
from time import sleep   # Импорт программы для замедления времени.

BANNER = '''
     Aesome BMI  

     '''


def BMI(weight, height):
    '''Функция определения BMI с введенными данными пользователя'''

    if float(weight) < + 1 or float(height) <= 0:
        print('Неправильные значения')

    return float(weight) / (float(height)/100)**2


def beauty_text(text1='', text2=''):
    '''Функция для всей логики'''

    sleep(2)
    print('+' + '_'*11 + '+')
    print('|' + ' '*11 + '|')
    print('|' + ' '*11 + '|')
    print('|' + text1 + '|')
    print('|' ' -=' + text2 + '=- ' '|')
    print('|' + ' '*11 + '|')
    print('|' + ' '*11 + '|')
    print('+' + '_'*11 + '+')
    sleep(2)


def logic_bmi(result):
    '''Функция'''

    sleep(2)
    if result < 18.5:
        return 'Ваш вес ниже нормального.'
    elif result >= 18.5 and result < 25.:
        return 'У вас нормальный вес.'
    elif result >= 25. and result < 30.:
        return 'У вас избыточный вес.'
    elif result >= 30. and result < 35.:
        return 'У вас ожирение 1 степени.'
    elif result >= 35. and result < 40.:
        return 'У вас ожирение 2 степени.'
    elif result >= 40.:
        return 'У вас ожирение 3 степени.'
    

def main():
    print(BANNER)
    beauty_text(' Find your', 'BMI')

    name = input('Введите ваше имя: ')
    weight = input('Введите ваш вес в кг.: ')
    height = input('Введите Ваш рост в см.: ')    

# Создание переменной с результатом функции. 
# Вызывает все внешние функции.
    result_bmi = BMI(weight, height)
    print(name + ',', 'ваш индекс массы тела: ', round(result_bmi, 2))

    print(logic_bmi(result_bmi))

    beauty_text(' -==BYE==- ')


if __name__ == '__main__':
    main()

        
    
