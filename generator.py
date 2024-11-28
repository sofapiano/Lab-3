import random as rand


ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNM'
def generate(code):
    code = [num for num in code]

    num1 = code[:3]
    num2 = code[3:]
    rand.shuffle(num1)
    rand.shuffle(num2)
    unit1, unit2 = '', ''

    for i in range(3):
        unit1 += num1[i]
        unit2 += num2[i]

    unit3 = str(int(unit1) + int(unit2))
    if len(unit3) == 1:
        unit3 = '000' + unit3
    elif len(unit3) == 2:
        unit3 = '00' + unit3
    elif len(unit3) == 3:
        unit3 = '0' + unit3
    
    for j in range(2):
        unit1 += rand.choice(ALPHABET)
        unit2 += rand.choice(ALPHABET)

    key = f'{unit1}-{unit2} {unit3}'

    return key


# print(generate(input()))    
'''1 и 2 блок должны содержать 4,5,6 и 1,2,3 цифры введенного числа соответственно, остальное - случайные буквы, 3 блок - результат сложения 
чисел, получившихся в 1 и 2 блоках. Пример: ввод «726911» -> 276DL-191GO-0467'''